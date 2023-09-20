import requests


def myWeather(data):
    mylist = []
    for key in data.items():
        my = "=".join(key)
        mylist.append(my)
    params = "?" + "&".join(mylist)
    url = 'https://www.baidu.com' + params
    print(url)

data = {
        "appid": "42928933",
        "appsecret": "Qtgjo71E",
        "cityid": "",
        "city": "北京",
        "ip": "",
        "callback": "",
        "vue": "1",
        "unescape": "1"
    }

myWeather(data)