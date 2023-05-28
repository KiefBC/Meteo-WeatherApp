import requests
import os
from dotenv import load_dotenv
from flask.views import MethodView
from flask import render_template, request
from main import db
from models import WeatherModel

# load our API key from our .env file
load_dotenv(override=True)


class MainIndexView(MethodView):
    def get(self):
        return render_template('index.html')

    def post(self):
        error = None
        city_name = request.form['city_name']
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')

        # check if request was successful
        if r.status_code == 200:
            data = r.json()
            data_obj = {
                'city': data['name'],
                'temp': self.kelvin_celcius(data['main']['temp']),
                'state': data['weather'][0]['main']
            }

            # required fields for the Model
            # required_fields = ['name']
            # for field in required_fields:
            #     if field not in data_obj:
            #         return f'Error: {field} not found in response'

            new_city = WeatherModel(name=city_name)
            db.session.add(new_city)
            db.session.commit()
            return render_template('index.html', data=data_obj)
        else:
            error = 'City not found'
            return render_template('index.html', error=error)

    @staticmethod
    def kelvin_celcius(kelvin: float) -> int:
        return int(kelvin - 273.15)


class ProfileView(MethodView):
    def get(self):
        return 'This is profile page'




class LoginView(MethodView):
    def get(self):
        return 'This is login page'


class AddCityView(MethodView):
    def get(self):
        return render_template('add_city.html')

    def post(self):
        error = None
        city_name = request.form['city_name']
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')

        # check if request was successful
        if r.status_code == 200:
            data = r.json()
            data_obj = {
                'city': data['name'],
                'temp': self.kelvin_celcius(data['main']['temp']),
                'state': data['weather'][0]['main']
            }

            # required fields for the Model
            # required_fields = ['name']
            # for field in required_fields:
            #     if field not in data_obj:
            #         return f'Error: {field} not found in response'

            new_city = WeatherModel(name=city_name)
            db.session.add(new_city)
            db.session.commit()
            return render_template('index.html', data=data_obj)
        else:
            error = 'City not found'
            return render_template('add_city.html', error=error)

    @staticmethod
    def kelvin_celcius(kelvin: float) -> int:
        return int(kelvin - 273.15)
