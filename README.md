# Weather App

## Video Demo: https://youtu.be/uE-Po-mkUA4

### About this project

In this Project we will use the OpenWeatherMap API to fetch the current weather of any city in the world, and then we will display the weather information on the screen. It is utilizing AJAX to build a more dynamic website. I have also incorporated API endpoints for viewing without the database, and the ability to delete entries from the database.

The Project is utilizing Flask and SQLAlchemy to do the heavy lifting.

As it stands, you will need to add your own API KEY in order to use this. In the future I will add a Prompt to do this for you. You can get an API KEY from https://openweathermap.org/api by signing up for a FREE account.

I found using AJAX to be pretty tricky at first. But as time went on and I kept using it, It got a lot easier. I feel pretty confident with the basics of AJAX now and how to properly use it within my Flask framework. I'd like to add more functionality and further develop my Database on this, because It was a lot of fun and I learned a lot.

Cacheing I think will be a fundamental thing going forward for me. I really like working on API Endpoints and being able to rehash the same data over and over is nice and no longer have to worry about API Key Banning or IP Banning from abusing ratelimits set by the API Provider. It was a bit tricky to understand at first and use, but now it is a bit more fluent for me.

I also much prefer using Classes to functions. OOP is being drilled into my skull everywhere I go and it just looks cleaner. Instead of a bunch of loose functions, we can create a Class for every "View" or rather "Page" that has a subset of methods within used only by that Page. This way I can modify code and methods without worry of breaking other parts of my project. It can be a little tricky sometimes remembering to do you `app.add_url_rule`.

I could have went a lot deeper with my Databases, but I just didn't know what else to add. We don't want to add temp values that are dynamic, which is why i just cache them instead. So that leaves me asking, what more is needed other than a City Name to speed up rehash of searches? Maybe I could add more GEO-Locational Data to filter results in the API more.

Splitting up my codebase into seperate files was hard. I was stuck in that circular import hell and I am so glad I figured it out.


#### Replace

`requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}')`

Put your API KEY in place of this exact block of text: `{os.getenv("API_KEY")}`

I did this because it is not a good idea to share API KEYs. Using the dotenv library allows you to hide/mask your API KEY from prying eyes. It is also fun just to be super sneaky and try and hide sensitive information.

## What I've Learned:

- How to use the OpenWeatherMap API to fetch the weather data.
- How to parse JSON data from a web service.
- How to use the JSON data to update the UI.
- How to use Flask to run a web application.
- How to use Jinja to render HTML templates.
- How to use Bootstrap to style a web application.
- How to use AJAX to fetch data from a web service asynchronously.

### Concepts used in this project:

- API
- JSON
- Flask
- Jinja
- Bootstrap
- AJAX
- Asynchronous Programming
- Web Scraping
- Web Development
- HTML
- CSS
- Python

## Future Ideas:

- Allow for more cities to be searched and added
- Add a 5-day forecast to each card using a Bootstrap Dropdown
- Add a toggle to switch between Fahrenheit and Celsius
- Add a toggle to switch between light and dark mode
- Add a toggle to switch between hourly and daily forecasts

