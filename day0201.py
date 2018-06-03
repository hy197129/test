# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:48:31 2018

@author: lenovo
"""




print('欢迎使用全球天气app')
print('1.查看当前城市天气  2.查看其他城市天气  3.保存当前城市')
menno=input('请输入菜单：')

if menno=='1':
    print('1.查看当前城市天气')
if menno=='2':
    print('2.查看其他城市天气')
if menno=='3':
    print('3.保存当前城市')
import urllib.request as r
city=input('请输入城市拼音：')
city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996  ".format(city)
info=r.urlopen(city_address).read().decode('utf-8','ignore')
            
import json
data=json.loads(info)
index=int(len(data['list']))
for i in range(0,index):
    day=data['list'][i]
    time=day['dt_txt']
    temp=day['main']['temp']
    description=day['weather'][0]['description']
    temp_max=day['main']['temp_max']
    pressure=day['main']['pressure']
    print('{}, 时间:{},  温度:{},  天气:{},  最高温度:{},  气压:{}'.format(city,time,temp,description,temp_max,pressure))
    print('-'*50)




