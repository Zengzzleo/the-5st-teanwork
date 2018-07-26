# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:21:16 2018

@author: user
"""

url='https://s.taobao.com/search?q=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8&ajax=true'
import urllib.request as r         #导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json               #将字符串转换为字典
data=json.loads(data)
#练习六1
def inf(a):
   b=data['mods']['itemlist']['data']['auctions'][a]['title']
   c=a+1
   print('第'+str(c)+'个商品信息为：')
   print((b))
   
for x in range(0,36):
   print(inf(x))
   if (x+1)%4==0:
        print('-'*50)
#练习六2
   for x in range(0,36):
       print(inf(x))       
    
#练习六3
p=[]
def price():
    for k in range(0,36):
        m=float(data['mods']['itemlist']['data']['auctions'][k]['view_price'] )
        p.append(m)
    return m
price()
i=sorted(p) 
print('价格从高到低排序结果：')
n=list(reversed(i))
print(n)
#练习六4
p=[]
def sales():
    for k in range(0,36):
        m=data['mods']['itemlist']['data']['auctions'][k]['view_sales']
        p.append((int(m[0:-3])))         
sales()
i=sorted(p)
print('销量从高到低排序结果：')
n=list(reversed(i))
print(n)

#练习六5  
def freefee():
    for i in range(0,36):
        if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'] )==0.0:
            print('第'+str(i+1)+'个商品包邮')      
freefee()