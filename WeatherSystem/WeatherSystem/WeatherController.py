from flask import jsonify, request
from Weather import Weather

# In-memory data store
weather_data_store = {}

class WeatherController:
    @staticmethod
    def register(app, weather_data_store):
        @app.route('/weather', methods=['POST'])
        def create_weather():
            data = request.json
            location = data['location']
            weather = Weather(location, data.get('temperature'), data.get('description'))
            weather_data_store[location] = weather
            return jsonify(weather.to_dict()), 201

        @app.route('/weather/<location>', methods=['GET'])
        def read_weather(location):
            weather = weather_data_store.get(location)
            if weather:
                return jsonify(weather.to_dict())
            return jsonify({"error": "Weather data not found"}), 404

        @app.route('/weather/<location>', methods=['PUT'])
        def update_weather(location):
            data = request.json
            weather = weather_data_store.get(location)
            if weather:
                weather.update_data(data)
                return jsonify(weather.to_dict())
            return jsonify({"error": "Weather data not found"}), 404

        @app.route('/weather/<location>', methods=['DELETE'])
        def delete_weather(location):
            if location in weather_data_store:
                del weather_data_store[location]
                return jsonify({"status": "success", "message": "Weather data deleted"})
            return jsonify({"error": "Weather data not found"}), 404

        @app.route('/weather/temperature/<location>', methods=['PUT'])
        def update_temperature(location):
            temperature = request.json.get('temperature')
            weather = weather_data_store.get(location)
            if weather:
                weather.temperature = temperature
                return jsonify(weather.to_dict())
            return jsonify({"error": "Weather data not found"}), 404

        @app.route('/weather/description/<location>', methods=['PUT'])
        def update_description(location):
            description = request.json.get('description')
            weather = weather_data_store.get(location)
            if weather:
                weather.description = description
                return jsonify(weather.to_dict())
            return jsonify({"error": "Weather data not found"}), 404

        @app.route('/weather/bulk_update', methods=['PUT'])
        def bulk_update_weather():
            updates = request.json
            for location, data in updates.items():
                weather = weather_data_store.get(location)
                if weather:
                    weather.update_data(data)
            return jsonify({"status": "success", "message": "Bulk update completed"}), 200
