class Weather:
    def __init__(self, location, temperature=None, description=None):
        self.location = location
        self.temperature = temperature
        self.description = description

    def update_data(self, data):
        self.temperature = data.get('temperature', self.temperature)
        self.description = data.get('description', self.description)

    def to_dict(self):
        return {
            "location": self.location,
            "temperature": self.temperature,
            "description": self.description
        }
