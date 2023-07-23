# Weather App

## Video Demo: https://youtu.be/uE-Po-mkUA4

### About this project

In this Project we will use the OpenWeatherMap API to fetch the current weather of any city in the world, and then we will display the weather information on the screen. It is utilizing AJAX to build a more dynamic website. I have also incorporated API endpoints for viewing without the database, and the ability to delete entries from the database.

The Project is utilizing Flask and SQLAlchemy to do the heavy lifting.

As it stands, you will need to add your own API KEY in order to use this. In the future I will add a Prompt to do this for you. You can get an API KEY from https://openweathermap.org/api by signing up for a FREE account.

## API Endpoints

- /api/delete/<int:id> - Deletes the entry with the given id from the database
- /api/<str:city> - Returns the weather data for the given city

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