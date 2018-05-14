class Location(object):
    def __init__(self, latitude: float, longitude: float, roadnumber: str):
        self.geocoordinates = {'latitude': latitude,
                               'longitude': longitude}
        self.roadnumber = roadnumber

    def get_value(self) -> dict:
        location_value = {
            "geoCoordinates": {
                "latitude": self.geocoordinates['latitude'],
                "longitude": self.geocoordinates['longitude']
            },
            "roadNumber": self.roadnumber
        }
        return location_value
