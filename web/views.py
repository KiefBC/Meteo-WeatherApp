import requests
import os
from dotenv import load_dotenv
from flask.views import MethodView
from flask import render_template, request
from models import WeatherModel, db
from flask import redirect, url_for
from cachetools import TTLCache, cached

load_dotenv(override=True)  # load our API key from our .env file
INDEX = 'index.html'
cache = TTLCache(maxsize=100, ttl=60)  # hold 100 items for 60 seconds


class MainIndexView(MethodView):
    def get(self):
        city_objs = self.fetch_cities()
        return render_template(INDEX, data=city_objs)

    def post(self):
        city_name = request.form['city_name']
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')

        # check if request was successful
        if r.status_code == 200:
            new_city = WeatherModel(name=city_name)
            db.session.add(new_city)
            db.session.commit()
            print('CITY ADDED')
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

    @staticmethod
    def kelvin_celcius(kelvin) -> int:
        return int(kelvin - 273.15)

    @cached(cache)
    # @cache.cached(timeout=60)
    def api_call(self, city_name: str) -> dict:
        data_object: list = []
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')
        data = r.json()
        data_obj = {
            'city': data['name'],
            'temp': self.kelvin_celcius(data['main']['temp']),
            'state': data['weather'][0]['main']
        }
        data_object.append(data_obj)
        return data_object

    def fetch_cities(self):
        cities = WeatherModel.query.all()
        city_objs = []
        for city in cities:
            city_obj: dict = {
                'city': city.name,
                'temp': self.api_call(city.name)[0]['temp'],
                'state': self.api_call(city.name)[0]['state']
            }
            city_objs.append(city_obj)
        return city_objs


class ProfileView(MethodView):
    def get(self):
        return 'This is profile page'


class LoginView(MethodView):
    def get(self):
        return 'This is login page'


class AddCityView(MethodView):
    def get(self):
        return render_template('add_city.html')
