from flask.views import MethodView
from flask import render_template


class MainIndexView(MethodView):
    def get(self):
        return render_template('index.html')


class ProfileView(MethodView):
    def get(self):
        return 'This is profile page'


class LoginView(MethodView):
    def get(self):
        return 'This is login page'
