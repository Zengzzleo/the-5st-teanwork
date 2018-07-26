# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:21:15 2018

@author: user
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'#联网天气代码
import urllib.request as r     #导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json    #将字符串转换为字典
data=json.loads(data)
for b in range(1,6): 
    a=2+(b-1)*8
    print('第'+str(b)+'天:')                   
    print('tempreture:'+str(data['list'][a]['main']['temp']))
    print('temp_max:'+str(data['list'][a]['main']['temp_max']))
    print('temp_min:'+str(data['list'][a]['main']['temp_min']))
    print('pressure:'+str(data['list'][a]['main']['pressure']))
    print('description:'+str(data['list'][a]['weather'][0]['description']))
    if str(data['list'][a]['weather'][0]['main'])=='clear':
        print('天气不错，出去走走')
    elif str(data['list'][a]['weather'][0]['main'])=='Clouds':
        print('阴天也要快乐')
    elif str(data['list'][a]['weather'][0]['main'])=='Rain':
        print('下雨天和巧克力更配哦')