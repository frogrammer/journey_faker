# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import json
from ..helpers import config, spatial

OUTPUT_FILE = config.CONFIG['MEETING_PLACES_FILE']

num_poi = config.CONFIG['NUM_MEETING_POIS']

random_latlngs = spatial.get_random_latlng_batch(num_poi)

random_meeting_places = [{'id': ll[0], 'latlng': ll[1]} for ll in enumerate(random_latlngs)]

mp_json = json.dumps(random_meeting_places)
with open(OUTPUT_FILE, 'w', encoding='UTF-8') as out_file:
    out_file.write(mp_json)
