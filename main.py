import requests

try:
    s_city = "Moscow,RU"
    appid = "cc40b8083ae820f97dcf5264dd7a94cc"


    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Прогноз погоды на неделю:")
    for i in data['list']:
        print("Дата <", i['dt_txt'],
              "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
              "> \r\nПогодные условия <", i['weather'][0]['description'],
              ">\r\nСкорость ветра <", i['wind']['speed'], ">")
        print("____________________________")
except requests.exceptions.ConnectionError:
    print('Проверьте соединение с интернетом')
