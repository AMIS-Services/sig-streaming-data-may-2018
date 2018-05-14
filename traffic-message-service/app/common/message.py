from datetime import datetime
from app.common.location import Location
from app.common.car import Car


class Message(object):
    def __init__(self, timestamp: datetime, location: Location, car: Car, speed: int):
        self.timestamp = timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
        self.location = location.get_value()
        self.car = car.get_value()
        self.speed = speed

    def get_value(self):
        the_message = {
            "timestamp": self.timestamp,
            "location": self.location,
            "car": self.car,
            "speed": self.speed
        }
        return the_message
