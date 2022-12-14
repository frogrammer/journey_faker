# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import random
import json
from app.helpers import config, spatial

OUTPUT_FILE = config.CONFIG['WAYPOINTS_FILE']
PEOPLE_FILE = config.CONFIG['PEOPLE_FILE']
num_journeys = config.CONFIG['NUM_JOURNEYS']
people_journeys = []
with open(PEOPLE_FILE, 'r', encoding='UTF-8') as pf:
    people_journeys = json.loads(pf.read())

for pj in [p for p in people_journeys if not 'story' in p]:
    pj['waypoints'] = [pj['start_place']]

random_latlngs = spatial.get_random_latlng_batch(num_journeys)
for ll in random_latlngs:
    pj = random.choice([p for p in people_journeys if not 'story' in p])
    pj['waypoints'].append(ll)

people_journeys_json = json.dumps(people_journeys)
with open(OUTPUT_FILE, 'w', encoding='UTF-8') as out_file:
    out_file.write(people_journeys_json)
