import requests
import os
from dotenv import load_dotenv
from flask.views import MethodView
from flask import render_template, request, flash
from models import WeatherModel, db
from flask import redirect, url_for
from cachetools import TTLCache, cached

load_dotenv(override=True)  # load our API key from our .env file
INDEX = 'index.html'
cache = TTLCache(maxsize=100, ttl=60)  # hold 100 items for 60 seconds


class MainIndexView(MethodView):
    def get(self):
        city_objs = self.fetch_cities()
        print(city_objs)
        return render_template(INDEX, data=city_objs)

    def post(self):
        city_name = request.form['input-city']
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')

        # check if request was successful
        if r.status_code == 200:
            existing_city = WeatherModel.query.filter_by(name=city_name).first()
            if existing_city:  # if city already exists
                flash('The city has already been added to the list!')
                return redirect(url_for('index'))
            new_city = WeatherModel(name=city_name)
            db.session.add(new_city)
            db.session.commit()
            flash('The city has been added to the list!')
            return redirect(url_for('index'))
        else:
            flash("The city doesn't exist!")
            return redirect(url_for('index'))

    @staticmethod
    def kelvin_celcius(kelvin) -> int:
        return int(kelvin - 273.15)

    @cached(cache)
    def api_call(self, city_name: str) -> list:
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
                'id': city.id,
                'city': city.name,
                'temp': self.api_call(city.name)[0]['temp'],
                'state': self.api_call(city.name)[0]['state']
            }
            city_objs.append(city_obj)
        return city_objs


class DeleteCity(MethodView):
    def post(self, city_id):
        city = WeatherModel.query.filter_by(id=city_id).first()
        if city:
            db.session.delete(city)
            db.session.commit()
            flash(f"{city.name} has been deleted.")
        else:
            flash(f"The city with ID '{city_id}' does not exist.")

        return redirect(url_for('index'))