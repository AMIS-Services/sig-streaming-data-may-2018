import random
import string
import csv
import os


# Constants
NUMBERS = list(range(48, 58))
ALPHABET = list(string.ascii_uppercase[:26])
INVALIDLETTERS = ['A', 'E', 'I', 'O', 'U', 'Q', 'Y']
INVALIDFIRSTLETTERS = INVALIDLETTERS + ['C', 'W']
VALIDLETTERS = [i for i in ALPHABET if i not in INVALIDLETTERS]
VALIDFIRSTLETTERS = [i for i in ALPHABET if i not in INVALIDFIRSTLETTERS]
LICENSEPLATE_TEMPLATES = ['XX-NNN-X', 'XX-NN-XX', 'NN-XXX-N', 'X-NNN-XX', 'XX-XX-NN', 'XX-XX-NN', 'NN-XX-XX', 'NN-NN-XX']
LICENSEPLATE_TEMPLATES_FOREIGN_B = ['1-NNN-XXX']
LICENSEPLATE_TEMPLATES_FOREIGN_D = ['K NN XXXXX', 'ST NNN XXX']
STATIC_FILEFOLDER = os.path.join('app', 'static')
CSV_DELIMITER = ';'
CSV_QUOTECHAR = '"'


class LicenceplateGenerator(object):
    def __init__(self, maximum: int=100):
        self.maxLicenses = maximum

    def generate_new_licenseplate(self, count: int=1):
        if count > self.maxLicenses:
            count = self.maxLicenses

        licenseplate_list = list()

        for i in range(count):
            # generate a foreign template 1 out of 10
            dice10 = random.randint(1, 10)
            if dice10 == 10:
                licenseplate_number = self.generate_licenseplate(LICENSEPLATE_TEMPLATES_FOREIGN_B)
                licenseplate_country = 'B'
            elif dice10 == 9:
                licenseplate_number = self.generate_licenseplate(LICENSEPLATE_TEMPLATES_FOREIGN_D)
                licenseplate_country = 'D'
            else:
                licenseplate_number = self.generate_licenseplate(LICENSEPLATE_TEMPLATES)
                licenseplate_country = 'NL'

            licenseplate_list.append((licenseplate_number, licenseplate_country))

        return licenseplate_list if len(licenseplate_list) > 1 else licenseplate_list[0]

    def generate_licenseplate(self, template: list):
        licenseplate_template = template[random.randrange(0, len(template))]
        licenseplate_number = ''
        for p in range(0, len(licenseplate_template)):
            if licenseplate_template[p][0] == 'N':
                if (p == 0) or (p > 0 and licenseplate_template[p - 1][0] == '-'):
                    licenseplate_number += VALIDFIRSTLETTERS[random.randrange(0, len(VALIDFIRSTLETTERS))]
                else:
                    licenseplate_number += VALIDLETTERS[random.randrange(0, len(VALIDLETTERS))]
            elif licenseplate_template[p][0] == 'X':
                if p == 0:
                    licenseplate_number += chr(NUMBERS[random.randrange(1, 10)])
                else:
                    licenseplate_number += chr(NUMBERS[random.randrange(0, 10)])
            else:
                licenseplate_number += licenseplate_template[p][0]
        return licenseplate_number


class CarColors(object):
    def __init__(self):
        self.colors = ['black'] * 10 + ['white'] * 8 + ['gray'] * 10 + ['blue'] * 6 + ['red'] * 3 + ['green'] * 3 + ['yellow']

    def get_random_color(self) -> str:
        return random.choice(self.colors)


class CarModels(object):
    def __init__(self, static_filefolder: str=STATIC_FILEFOLDER):
        self.file_folder = static_filefolder
        self.carmodels = list()
        self.read_csv_file()

    def read_csv_file(self, file_name: str = 'carmodels.csv'):
        file_path = os.path.join(self.file_folder, file_name)
        with open(file_path) as csvfile:
            carmodels = csv.reader(csvfile, delimiter=CSV_DELIMITER, quotechar=CSV_QUOTECHAR)
            for carmodel_record in carmodels:
                carmodel = {"manufacturer": carmodel_record[0],
                            "model": carmodel_record[1],
                            "type": 'P' if carmodel_record[2] == '' else carmodel_record[2]
                            }
                self.carmodels.append(carmodel)

    def get_random_carmodel(self) -> dict:
        random_index = random.randint(0, len(self.carmodels)-1)
        random_car = dict(self.carmodels[random_index])
        return random_car


class Locations(object):
    def __init__(self, static_filefolder: str=STATIC_FILEFOLDER):
        self.file_folder = static_filefolder
        self.locations = list()
        self.read_csv_file()

    def read_csv_file(self, file_name: str = 'locations.csv'):
        file_path = os.path.join(self.file_folder, file_name)
        with open(file_path) as csvfile:
            locations = csv.reader(csvfile, delimiter=CSV_DELIMITER, quotechar=CSV_QUOTECHAR)
            for location_record in locations:
                location = {"road_number": location_record[0],
                            "latitude": location_record[1],
                            "longitude": location_record[2]
                            }
                self.locations.append(location)

    def get_random_location(self, roadnumber=None) -> dict:
        if roadnumber is None:
            random_index = random.randint(0, len(self.locations)-1)
            random_location = dict(self.locations[random_index])
        else:
            filtered_locations = list()
            for location in self.locations:
                if location['road_number'] == roadnumber:
                    filtered_locations.append(location)
            random_index = random.randint(0, len(filtered_locations)-1)
            random_location = dict(filtered_locations[random_index])

        return random_location
