import requests
import os
from dotenv import load_dotenv
from flask.views import MethodView
from flask import render_template, request, flash, jsonify
from models import WeatherModel, db
from flask import redirect, url_for
from cachetools import TTLCache, cached

load_dotenv(override=True)  # load our API key from our .env file
INDEX = 'index.html'
# Cache so we don't get rate limited
cache = TTLCache(maxsize=100, ttl=60)  # hold 100 items for 60 seconds


class MainIndexView(MethodView):
    """
    Main Page View
    """

    def get(self):
        city_objs = self.fetch_cities()
        print(city_objs)
        return render_template(INDEX, data=city_objs)

    @staticmethod
    def post():
        # if form submission is json
        if request.is_json:
            city_name = request.json['city']
        else:
            city_name = request.form['input-city']

        # make request to API and grabbing our API key from our .env file
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')

        # check if request was successful
        if r.status_code == 200:

            # Check if city already exists in database
            existing_city = WeatherModel.query.filter_by(name=city_name).first()
            if existing_city:
                flash('The city has already been added to the list!')
                return redirect(url_for('index'))

            else:  # Add the new city to database
                new_city = WeatherModel(name=city_name)
                db.session.add(new_city)
                db.session.commit()
                flash('The city has been added to the list!')
                return redirect(url_for('index'))

        # if request was unsuccessful
        else:
            flash("The city doesn't exist!")
            return redirect(url_for('index'))

    @staticmethod
    def kelvin_celcius(kelvin) -> int:
        """
        Converts Kelvin to Celcius
        :param kelvin: int
        :return: int
        """

        # Round to 2 decimal places
        celcius: int = round(kelvin - 273.15, 2)
        return celcius

    @staticmethod
    def fetch_cities(self):
        """
        Fetches all cities from the database
        :return:
        """
        cities = WeatherModel.query.all()
        city_objs = []
        for city in cities:
            city_obj: dict = {
                'id': city.id,
                'city': city.name,
                'temp': api_call(city.name)[0]['temp'],
                'state': api_call(city.name)[0]['state']
            }
            city_objs.append(city_obj)
        return city_objs


class DeleteCity(MethodView):
    """
    Deletes a city from the database
    """

    @staticmethod
    def post(city_id: str):
        city = WeatherModel.query.filter_by(id=city_id).first()
        if city:
            db.session.delete(city)
            db.session.commit()
            flash(f"{city.name} has been deleted.")
        else:
            flash(f"The city with ID '{city_id}' does not exist.")

        return redirect(url_for('index'))


class WeatherAPIView(MethodView):
    """
    View Weather Data from API
    """

    @staticmethod
    def get(city_name: str):
        """
        Makes a call to the OpenWeatherMap API
        :param city_name:
        :return:
        """

        # Check if city_name has 2 words "New York" vs "Boston"
        if len(city_name.split()) > 1:
            city_name = city_name.replace(" ", "%20")

        # Check if City Exists in the API Provider
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')
        city_data = r.json()

        # Check if city exists
        if city_data['cod'] == 200:
            data_obj = {
                'city': city_data['name'],
                'temp': MainIndexView.kelvin_celcius(city_data['main']['temp']),
                'state': city_data['weather'][0]['main']
            }
            return jsonify(data_obj)
        else:
            return jsonify({'error': 'City not found!'}), 404

    @staticmethod
    def post(city_id: int):

        # Check if city exists
        city = WeatherModel.query.get(city_id)
        if city:
            db.session.delete(city)
            db.session.commit()

            # Create a response object
            response = {
                'message': f"{city.name} has been deleted."
            }
            return jsonify(response), 200

        else:
            response = {
                'message': f"The city with ID '{city_id}' does not exist."
            }
            return jsonify(response), 404


class WeatherAPIDeleteView(MethodView):
    """
    Deletes a city from the database using the API
    """
    @staticmethod
    def post(city_id: str):

        # Check if city exists
        city = WeatherModel.query.filter_by(id=city_id).first()
        if city:
            db.session.delete(city)
            db.session.commit()

            # Create a response object
            response = {
                'message': f"{city.name} has been deleted."
            }

        # If city does not exist
        else:
            response = {
                'message': f"The city with ID '{city_id}' does not exist."
            }

        return jsonify(response), 200


@cached(cache)
def api_call(city_name: str) -> list:
    """
    Makes a call to the OpenWeatherMap API
    :param city_name:
    :return:
    """
    data_object: list = []
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')
    data = r.json()
    data_obj = {
        'city': data['name'],
        'temp': MainIndexView.kelvin_celcius(data['main']['temp']),
        'state': data['weather'][0]['main']
    }
    data_object.append(data_obj)
    return data_object
