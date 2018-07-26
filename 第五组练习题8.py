# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:21:15 2018

@author: user
"""

import urllib.request as r      #导入联网工具包，名为为r
import json         #将字符串转换为字典
for a in range(1,101):
    b=(a-1)*44
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E6%B5%99%E6%B1%9F&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s='+str(b)+'&ajax=true'
    c=r.urlopen(url).read().decode('utf-8','ignore')
    c=json.loads(c)
    f=open('淘宝数据-浙江.txt','a',encoding='utf-8')
    f.write(str(c)+'\n')
    print('成功爬取第'+str(a)+'条数据')
f.close()
