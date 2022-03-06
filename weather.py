from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request

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
    source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + api).read()


    # converting JSON data to a dictionary
    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "cityname": city,
        "icon": ("https://openweathermap.org/img/wn/"+str(list_of_data['weather'][0]['icon']+".png")),
        "desc": str(list_of_data['weather'][0]['description']),
        "temp": str(round(list_of_data['main']['temp'], 2)) + '°C',
        "wind": str(list_of_data['wind']['speed']) + ' km/h',
        "humidity": str(list_of_data['main']['humidity']),
        "backgroundImage": "('https://source.unsplash.com/1600x900/?" + city + "')",

    }

    print(data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
