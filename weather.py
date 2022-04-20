from flask import Flask, render_template, request
from datetime import datetime
import requests

# import json to load JSON data to a python dictionary
# import json


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])

def weather():
    global city,api,source2,source,list_of_data,response,current_weather,response1,now
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name bhopal
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

    return render_template('index.html', data=data)
@app.route("/details", methods=['POST', 'GET'])

def weather1():
   if response & response1 != 200:
     data = 'City not found'
   else:
     data = {
         "cityname": city,
         "d_text": str(now.strftime("%Y-%m-%d")),
         "t_text": str(now.strftime("%H:%M:%S")),

         "icon1": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][0]['weather'][0]['icon'] + ".png")),
         "temp1": str(round(list_of_data['list'][0]['main']['temp'])) + '°C',
         "dt_text1": str(list_of_data['list'][0]['dt_txt']),
         "desc1": str(list_of_data['list'][0]['weather'][0]['description']),

         "icon2": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][3]['weather'][0]['icon'] + ".png")),
         "temp2": str(round(list_of_data['list'][3]['main']['temp'])) + '°C',
         "dt_text2": str(list_of_data['list'][3]['dt_txt']),
         "desc2": str(list_of_data['list'][3]['weather'][0]['description']),

         "icon3": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][6]['weather'][0]['icon'] + ".png")),
         "temp3": str(round(list_of_data['list'][6]['main']['temp'])) + '°C',
         "dt_text3": str(list_of_data['list'][6]['dt_txt']),
         "desc3": str(list_of_data['list'][6]['weather'][0]['description']),

         "icon4": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][9]['weather'][0]['icon'] + ".png")),
         "temp4": str(round(list_of_data['list'][9]['main']['temp'])) + '°C',
         "dt_text4": str(list_of_data['list'][9]['dt_txt']),
         "desc4": str(list_of_data['list'][9]['weather'][0]['description']),

         "icon5": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][12]['weather'][0]['icon'] + ".png")),
         "temp5": str(round(list_of_data['list'][12]['main']['temp'])) + '°C',
         "dt_text5": str(list_of_data['list'][12]['dt_txt']),
         "desc5": str(list_of_data['list'][12]['weather'][0]['description']),

         "icon6": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][15]['weather'][0]['icon'] + ".png")),
         "temp6": str(round(list_of_data['list'][15]['main']['temp'])) + '°C',
         "dt_text6": str(list_of_data['list'][15]['dt_txt']),
         "desc6": str(list_of_data['list'][15]['weather'][0]['description']),

         "icon7": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][18]['weather'][0]['icon'] + ".png")),
         "temp7": str(round(list_of_data['list'][18]['main']['temp'])) + '°C',
         "dt_text7": str(list_of_data['list'][18]['dt_txt']),
         "desc7": str(list_of_data['list'][18]['weather'][0]['description']),

         "icon8": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][21]['weather'][0]['icon'] + ".png")),
         "temp8": str(round(list_of_data['list'][21]['main']['temp'])) + '°C',
         "dt_text8": str(list_of_data['list'][21]['dt_txt']),
         "desc8": str(list_of_data['list'][21]['weather'][0]['description']),

         "icon9": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][24]['weather'][0]['icon'] + ".png")),
         "temp9": str(round(list_of_data['list'][24]['main']['temp'])) + '°C',
         "dt_text9": str(list_of_data['list'][24]['dt_txt']),
         "desc9": str(list_of_data['list'][24]['weather'][0]['description']),

         "icon10": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][27]['weather'][0]['icon'] + ".png")),
         "temp10": str(round(list_of_data['list'][27]['main']['temp'])) + '°C',
         "dt_text10": str(list_of_data['list'][27]['dt_txt']),
         "desc10": str(list_of_data['list'][27]['weather'][0]['description']),

         "icon11": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][30]['weather'][0]['icon'] + ".png")),
         "temp11": str(round(list_of_data['list'][30]['main']['temp'])) + '°C',
         "dt_text11": str(list_of_data['list'][30]['dt_txt']),
         "desc11": str(list_of_data['list'][30]['weather'][0]['description']),

         "icon12": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][33]['weather'][0]['icon'] + ".png")),
         "temp12": str(round(list_of_data['list'][33]['main']['temp'])) + '°C',
         "dt_text12": str(list_of_data['list'][33]['dt_txt']),
         "desc12": str(list_of_data['list'][33]['weather'][0]['description']),

         "icon13": ("https://openweathermap.org/img/wn/" + str(list_of_data['list'][36]['weather'][0]['icon'] + ".png")),
         "temp13": str(round(list_of_data['list'][36]['main']['temp'])) + '°C',
         "dt_text13": str(list_of_data['list'][36]['dt_txt']),
         "desc13": str(list_of_data['list'][36]['weather'][0]['description']),

         "icon14": ("https://openweathermap.org/img/wn/" + str(
             list_of_data['list'][39]['weather'][0]['icon'] + ".png")),
         "temp14": str(round(list_of_data['list'][39]['main']['temp'])) + '°C',
         "dt_text14": str(list_of_data['list'][39]['dt_txt']),
         "desc14": str(list_of_data['list'][39]['weather'][0]['description']),
         }

     return render_template('details.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
