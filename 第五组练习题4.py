# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:57:30 2018

@author: 10257
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=mianyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'#联网天气代码
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
#1.打印每天18点的天气信息，温度，程序，情况，气压，最高温度，最低温度
print('第一天')#data->list->5 index->main->temp
print('气温'+str(data['list'][5]['main']['temp']))
print('最低气温'+str(data['list'][5]['main']['temp_min']))
print('最高气温'+str(data['list'][5]['main']['temp_max']))
print('天气状况'+str(data['list'][5]['weather'][0]['main']))
print('气压'+str(data['list'][5]['main']['pressure']))
#########
print('第二天')
print('气温'+str(data['list'][13]['main']['temp']))
print('最低气温'+str(data['list'][13]['main']['temp_min']))
print('最高气温'+str(data['list'][13]['main']['temp_max']))
print('天气状况'+str(data['list'][13]['weather'][0]['main']))
print('气压'+str(data['list'][13]['main']['pressure']))
########
print('第三天')
print('气温'+str(data['list'][21]['main']['temp']))
print('最低气温'+str(data['list'][21]['main']['temp_min']))
print('最高气温'+str(data['list'][21]['main']['temp_max']))
print('天气状况'+str(data['list'][21]['weather'][0]['main']))
print('气压'+str(data['list'][21]['main']['pressure']))
########
print('第四天')
print('气温'+str(data['list'][29]['main']['temp']))
print('最低气温'+str(data['list'][29]['main']['temp_min']))
print('最高气温'+str(data['list'][29]['main']['temp_max']))
print('天气状况'+str(data['list'][29]['weather'][0]['main']))
print('气压'+str(data['list'][29]['main']['pressure']))
########
print('第五天')
print('气温'+str(data['list'][37]['main']['temp']))
print('最低气温'+str(data['list'][37]['main']['temp_min']))
print('最高气温'+str(data['list'][37]['main']['temp_max']))
print('天气状况'+str(data['list'][37]['weather'][0]['main']))
print('气压'+str(data['list'][37]['main']['pressure']))

##打印温度折线图
a=data['list'][5]['main']['temp']
b=data['list'][13]['main']['temp']
c=data['list'][21]['main']['temp']
d=data['list'][29]['main']['temp']
e=data['list'][37]['main']['temp']
print('温度折线图：')
print('第一天:'+'-'*int(a))
print('第二天:'+'-'*int(b))
print('第三天:'+'-'*int(c))
print('第四天:'+'-'*int(d))
print('第五天:'+'-'*int(e))
##############
##获取所有的温度，并且排序（sorted([1,4,-1,8])###使用此方法排序）
print('温度排序')
sorted([a,b,c,d,e])