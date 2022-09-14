# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import json
from faker import Faker
from .helpers import config, spatial

OUTPUT_FILE = config.CONFIG['PEOPLE_FILE']
num_people = config.CONFIG['NUM_PEOPLE']
faker = Faker()

random_latlngs = spatial.get_random_latlng_batch(num_people)

random_people = [{'id': ll[0], 'name': faker.name(), 'favourite_place': ll[1]} for ll in enumerate(random_latlngs)]
people_json = json.dumps(random_people)
with open(OUTPUT_FILE, 'w', encoding='UTF-8') as out_file:
    out_file.write(people_json)
