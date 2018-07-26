# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:24:25 2018

@author: user
"""
ls=open('school_id.txt',encoding='utf-8').readlines()

schoolls=[]

for line in ls:
    schoolls.append(line)
    
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest'}
f=open('全国招生人数.txt','a',encoding='utf-8')
for schoolid in ls:
    for kemu in[1,2]:
        for city in[62,63,64,65]:
            req=r.Request(url,data='id={}&type={}&city={}&state=1'.format(schoolid,kemu,city).encode(),headers=headers)
            f.write(r.urlopen(req).read().decode('utf-8','ignore')+'\n')
f.close()   
