# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:48:31 2018

@author: lenovo
"""




import urllib.request as r
city_pinyin=input('请输入城市拼音：')
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')


import json
data=json.loads(info)

for j in range(0,6):
    for i in range(0,7):
        data0=data['list'][i+j*8]['dt_txt']
        data1=data['list'][i+j*8]['main']['temp_min']
        data2=data['list'][i+j*8]['main']['temp_max']
        data3=data['list'][i+j*8]['weather'][0]['description']
        print(city_pinyin)
        print('时间：'+data0+'\t')
        print('温度：'+str(data1)+'~'+str(data2)+'\t')
        print('天气状况：'+data3+'\t')

        print('\t'*2)
    print('*'*50)










