import sys
from views import MainIndexView, LoginView, ProfileView, AddCityView
from models import db, app

app.add_url_rule('/', view_func=MainIndexView.as_view('index'))
app.add_url_rule('/login', view_func=LoginView.as_view('login'))
app.add_url_rule('/profile', view_func=ProfileView.as_view('profile'))
app.add_url_rule('/', view_func=AddCityView.as_view('add_city'))

with app.app_context():
    db.drop_all()
    db.create_all()


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
