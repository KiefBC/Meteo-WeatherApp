from flask.views import MethodView
from flask import render_template, request


class MainIndexView(MethodView):
    def get(self):
        return render_template('index.html')


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
        city_name = request.form['city_name']
        return 'City Added!!!!!!!!!!!!!'
