from flask import Flask, render_template, request
from datetime import datetime
import requests

# import json to load JSON data to a python dictionary
import json


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name mathura
        city = 'Bhopal'

    # your API key will come here
    api = "8f175536dc374b00de60501797e5fff8"

    # source contain json data from api
    source2 = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + api)
    source = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&units=metric&appid=" + api)


    # converting JSON data to a dictionary
    list_of_data = source.json()
    response = source.status_code
    current_weather = source2.json()
    response1 = source2.status_code
    now = datetime.now()


    if response & response1 != 200:
     data = 'City not found'
    # data for variable list_of_data
    else:
     data = {
        "cityname": city,
        "icon": ("https://openweathermap.org/img/wn/"+str(current_weather['weather'][0]['icon']+".png")),
        "desc": str(current_weather['weather'][0]['description']),
        "temp": str(round(current_weather['main']['temp'], 2)) + '°C',
        "wind": str(current_weather['wind']['speed']) + ' km/h',
        "humidity": str(current_weather['main']['humidity']),
        "d_text": str(now.strftime("%Y-%m-%d")),
        "t_text": str(now.strftime("%H:%M:%S")),

        "icon1": ("https://openweathermap.org/img/wn/"+str(list_of_data['list'][2]['weather'][0]['icon']+".png")),
        "temp1": str(round(list_of_data['list'][2]['main']['temp'])) + '°C',
        "dt_text1": str(list_of_data['list'][2]['dt_txt']),
        "desc1": str(list_of_data['list'][2]['weather'][0]['description']),

        "icon2": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][10]['weather'][0]['icon'] + ".png")),
        "temp2": str(round(list_of_data['list'][10]['main']['temp'])) + '°C',
        "dt_text2": str(list_of_data['list'][10]['dt_txt']),
        "desc2": str(list_of_data['list'][10]['weather'][0]['description']),

        "icon3": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][14]['weather'][0]['icon'] + ".png")),
        "temp3": str(round(list_of_data['list'][14]['main']['temp'])) + '°C',
        "dt_text3": str(list_of_data['list'][14]['dt_txt']),
        "desc3": str(list_of_data['list'][14]['weather'][0]['description']),

        "icon4": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][18]['weather'][0]['icon'] + ".png")),
        "temp4": str(round(list_of_data['list'][18]['main']['temp'])) + '°C',
        "dt_text4": str(list_of_data['list'][18]['dt_txt']),
        "desc4": str(list_of_data['list'][18]['weather'][0]['description']),

        "icon5": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][22]['weather'][0]['icon'] + ".png")),
        "temp5": str(round(list_of_data['list'][22]['main']['temp'])) + '°C',
        "dt_text5": str(list_of_data['list'][22]['dt_txt']),
        "desc5": str(list_of_data['list'][22]['weather'][0]['description']),

        "icon6": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][26]['weather'][0]['icon'] + ".png")),
        "temp6": str(round(list_of_data['list'][26]['main']['temp'])) + '°C',
        "dt_text6": str(list_of_data['list'][26]['dt_txt']),
        "desc6": str(list_of_data['list'][26]['weather'][0]['description']),

        "icon7": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][30]['weather'][0]['icon'] + ".png")),
        "temp7": str(round(list_of_data['list'][30]['main']['temp'])) + '°C',
        "dt_text7": str(list_of_data['list'][30]['dt_txt']),
        "desc7": str(list_of_data['list'][30]['weather'][0]['description'])
        }

    print(data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
