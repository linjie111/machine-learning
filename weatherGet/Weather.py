import requests, json

#  notice  api地址
import CalDate

url = 'http://t.weather.sojson.com/api/weather/city/'

# weather api

response = requests.get(url + '101250101')
r = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?city=430121&key=b99f40bd4e3f03a9f66f1e04acbfa91a&extensions=all')
r.encoding='utf-8'
cc = r.json()
city = cc['forecasts'][0]['province']+cc['forecasts'][0]['city']
nowTime = cc['forecasts'][0]['reporttime']
weather = "白天 ："+cc['forecasts'][0]['casts'][0]['dayweather'] +"   晚上 ："+cc['forecasts'][0]['casts'][0]['nightweather']
tem = cc['forecasts'][0]['casts'][0]['nighttemp']+"°c ~ "+cc['forecasts'][0]['casts'][0]['daytemp']+"°c"

#将数据以json形式返回，这个d就是返回的json数据
d = response.json()

#当返回状态码为200，输出天气状况
if(d['status'] == 200):
    notice = d["data"]["forecast"][0]["notice"]

time = "我和迪哥的第  "+ str(CalDate.Cal_Date()) + " day "