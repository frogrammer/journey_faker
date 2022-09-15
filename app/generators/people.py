# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import json
from random import randint
from faker import Faker
from app.generators import devices
from app.helpers import config, file, spatial

PEOPLE_STORY_FILE = config.CONFIG['PEOPLE_STORY_FILE']
OUTPUT_FILE = config.CONFIG['PEOPLE_FILE']

num_people = config.CONFIG['NUM_PEOPLE']

faker = Faker()

story_people = file.read_json(PEOPLE_STORY_FILE)
random_latlngs = spatial.get_random_latlng_batch(num_people)
ids = [i for i in  range(0, num_people + len(story_people)) if i not in [p['id'] for p in story_people]]

story_people = file.read_json(PEOPLE_STORY_FILE)

for p in story_people:
    p['devices'] = devices.generate_devices()
    p['known_wifi'] = devices.generate_known_wifi()
    p['story'] = True

random_people = [{
        'id': ids[ll[0]], 
        'name': faker.name(), 
        'devices': devices.generate_devices(), 
        'known_wifi': devices.generate_known_wifi(), 
        'start_place': ll[1]} 
    for ll in enumerate(random_latlngs)]

file.write_json(OUTPUT_FILE, story_people + random_people)
