from main import app
from views import MainIndexView, ProfileView, LoginView, AddCityView
import sys

app.add_url_rule('/', view_func=MainIndexView.as_view('index'))
app.add_url_rule('/login', view_func=LoginView.as_view('login'))
app.add_url_rule('/profile', view_func=ProfileView.as_view('profile'))
app.add_url_rule('/add', view_func=AddCityView.as_view('add_city'))



# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
