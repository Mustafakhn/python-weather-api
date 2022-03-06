from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import requests


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name BHOPAL
        city = 'Bhopal'

    # your API key will come here
    api = "8f175536dc374b00de60501797e5fff8"

    # source contain json data from api
    # source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + api).read()
    source = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + api)
    response = source.status_code
    print(str(response))
    # converting JSON data to a dictionary

    list_of_data = source.json()

    if response != 200:
     data = {list_of_data['message']}
    # data for variable list_of_data
    else:
        data = {
         "cityname": city,
         "icon": ("https://openweathermap.org/img/wn/"+str(list_of_data['weather'][0]['icon']+".png")),
         "desc": str(list_of_data['weather'][0]['description']),
         "temp": str(round(list_of_data['main']['temp'], 2)) + '°C',
         "wind": str(list_of_data['wind']['speed']) + ' km/h',
         "humidity": str(list_of_data['main']['humidity']),
         "backgroundImage": "('https://source.unsplash.com/1600x900/?" + city + "')",

     }
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
