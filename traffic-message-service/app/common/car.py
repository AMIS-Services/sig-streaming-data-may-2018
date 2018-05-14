import random


class Car(object):
    def __init__(self, marque: str, model: str, color: str, licenseplate_number: str, country_code: str):
        self.marque = marque
        self.model = model
        self.color = color.lower()
        self.country_code = country_code.upper()
        self.licenseplate_number = licenseplate_number

    def get_value(self) -> dict:
        car_value = {
            "licenseplate": self.licenseplate_number[0],
            "country": self.licenseplate_number[1],
            "manufacturer": self.marque,
            "model": self.model,
            "color": self.color
        }
        return car_value

    def get_random_speed(self, minimum_speed: int=80, maximum_speed: int=140):
        random_speed = random.randint(minimum_speed, maximum_speed)
        return random_speed
