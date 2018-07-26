# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:50:50 2018

@author: user
"""

import urllib.request as r
import json
q='chengdu'
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+q+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
data = json.loads(data) 
print('description:'+data['weather'][0]['description'])
print('temp:'+str(data['main']['temp']))
print('pressure:'+str(data['main']['pressure']))