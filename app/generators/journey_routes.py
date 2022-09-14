# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import random
import json
from app.helpers import config, spatial

OUTPUT_FILE = config.CONFIG['JOURNEY_ROUTES_FILE']
JOURNEYS_FILE = config.CONFIG['PEOPLE_JOURNEYS_FILE']

journeys = []
with open(JOURNEYS_FILE, 'r', encoding='UTF-8') as jf:
    journeys = json.loads(jf.read())

test = journeys[0]['journeys']
routes = spatial.get_route(test)
routes