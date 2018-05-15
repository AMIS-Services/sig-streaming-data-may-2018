from flask import request, jsonify
from flask import Blueprint
from app.generators import LicenceplateGenerator, CarColors, CarModels, Locations
from app.common.message import Message, Car, Location
from datetime import datetime, timedelta


traffic = Blueprint('traffic', __name__)
DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


@traffic.route("/licenseplates")
def get_license_plates():
    gen = LicenceplateGenerator()
    number_of_plates = int(request.args.get('count', 1))
    the_plates = gen.generate_new_licenseplate(number_of_plates)
    response = jsonify(the_plates)
    return response


@traffic.route("/")
def get_traffic_messages():
    gen = LicenceplateGenerator()
    car_models = CarModels()
    locations = Locations()
    car_colors = CarColors()
    messages = list()

    # Get request parameters
    number_of_messages = int(request.args.get('count', 1))
    random_location = request.args.get('randomlocation', 'false')
    select_random_location = True if random_location.capitalize() == 'True' else False
    start_timestamp = request.args.get('starttime', datetime.today().strftime(DATE_FORMAT))
    stepsize_timestamp = int(request.args.get('time_stepsize', 2300))  # Timestamp step size in millisec
    timestamp_delta = timedelta(milliseconds=stepsize_timestamp)
    roadnumber = request.args.get('roadnumber', None)
    if not select_random_location:
        random_location = locations.get_random_location(roadnumber)

    message_timestamp = datetime.strptime(start_timestamp, DATE_FORMAT)
    for i in range(number_of_messages):
        car_color = car_colors.get_random_color()
        car_model = car_models.get_random_carmodel()
        if select_random_location:
            random_location = locations.get_random_location(roadnumber)
        location = Location(random_location["latitude"], random_location["longitude"], random_location["road_number"])
        license_plate = gen.generate_new_licenseplate()
        car = Car(car_model["manufacturer"], car_model["model"], car_color, license_plate, 'NL')
        speed = car.get_random_speed()
        message_timestamp += timestamp_delta
        traffic_message = Message(message_timestamp, location, car, speed)
        messages.append(traffic_message.get_value())

    response = jsonify(messages)
    return response

