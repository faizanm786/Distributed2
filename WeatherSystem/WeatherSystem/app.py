from flask import Flask
from WeatherController import WeatherController
from Weather import Weather

app = Flask(__name__)

# Dummy data initialization
weather_data_store = {
    "New York": Weather("New York", 15, "Partly cloudy").to_dict(),
    "London": Weather("London", 10, "Rainy").to_dict(),
    "Tokyo": Weather("Tokyo", 20, "Sunny").to_dict()
}

# Initialize the routes
WeatherController.register(app, weather_data_store)

if __name__ == '__main__':
    app.run(debug=True)
