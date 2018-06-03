# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:28:51 2018

快捷键，字体放大
ctrl +
新建python文件
ctrl +new 
保存

执行代码，选中代码，ctrl + enter
查看python版本Python 3.6.2
@author: yq
"""
#一次申请一个变量
a=3
#一次申明多个变量
xuan,guibin,xixi=80,90,88
xj='小娇'
yanzhi=5.44444444444
#自动补全代码 按  Tab
#TypeError: must be str, not float
print(xj+yanzhi)
#将其他类型转换成字符串类型
b=str(yanzhi)
c='3.9'
d=float(c)
print(xj+str(yanzhi))

print(xj+'\t'+str(yanzhi))

#字符串中出现{}大括号，表示是占位符
print('今天温度是{}天气是{}今天星期{}'.format(10,'小雨','六'))
"""
"""
#列表list,
usemoney=12,20,30,19,20
usemoney[1]
usemoney2=[12,20,30,19,20]
print(usemoney2[0])

list=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print('今天是：'+list[5])
print(list[6])


msg={'地址':'北京市海淀区xxxx',
 '手机号码':'17828791577',
 '寄信人':'chance'}
print(msg['地址'])
print(msg['手机号码'])
print(msg['寄信人'])

body={'姓名':'HY',
      '身高':'166',
      '性别':'女',
      '年龄':'20'}
print(body['姓名'])
print(body['身高'])
print(body['性别'])
print(body['年龄'])


xue={'name':'薛之谦',
     'songs':['演员','绅士','丑八怪','认真的雪','动物世界'],
     '昵称':'阿薛',
     '认识过女朋友':['2','8','1','4','9']}
songs=xue['songs']
print(songs)
print(len(songs))
print(max(xue['认识过女朋友']))


weather={'天气':'阴',
         '未来5天的温度':['25','22','27','30','28'],
         '未来5天的情况':['阴','小雨','晴','晴','多云'],
         '今天':'星期六'
        }

print('今天的天气：'+weather['天气'])
print(weather['未来5天的温度'])
print(weather['未来5天的情况'])
print('今天是：'+weather['今天'])
print('未来5天最高气温：'+max(weather['未来5天的温度']))





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
city_pinyin=input('请输入城市拼音：')
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996 '
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')


import json
data=json.loads(info)

data['main']['temp']
data['main']['temp_max']
data['main']['pressure']
data['weather'][0]['description']

print('温度：'+str(data['main']['temp']))
print('最高气温：'+str(data['main']['temp_max']))
print('气压：'+str(data['main']['pressure']))
print('天气：'+str(data['weather'][0]['description']))




import urllib.request as r
city_pinyin=input('请输入城市拼音：')
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')


import json
data=json.loads(info)
data1=data['list']
data2=data1['0']['main']['temp']

data['main']['temp']
data['main']['temp_max']
data['main']['pressure']
data['weather'][0]['description']

print('温度：'+str(data['main']['temp']))
print('最高气温：'+str(data['main']['temp_max']))
print('气压：'+str(data['main']['pressure']))
print('天气：'+str(data['weather'][0]['description']))






















