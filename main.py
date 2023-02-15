import socket

import requests
try:
    s_city = "Moscow,RU"
    appid = "cc40b8083ae820f97dcf5264dd7a94cc"

    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Город :", s_city)
    print("Погодные условия :", (data['weather'][0]['description']).upper())
    print("Температура :", data['main']['temp'] , 'C°')
    print("Минимальная температура :", data['main']['temp_min'] , 'C°')
    print("Максимальная температура :", data['main']['temp_max'], 'C°')
    print("Температура ощущается как:", data['main']['feels_like'] , 'C°')
    print('Видимость :' , data['visibility'] , 'м')
    print('Скорость ветра :' , data['wind']['speed'] , 'м/с')
    print('Порыв ветра :' , data['wind']['gust'] , 'м/с')
except requests.exceptions.ConnectionError:
    print('Проверьте соединение с интернетом')
