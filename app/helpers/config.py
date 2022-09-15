# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_CONFIG = {
    'CENTRE_LAT':0.0,
    'CENTRE_LNG':0.0,
    'RADIUS_KM': 5,
    'NUM_JOURNEYS': 10,
    'NUM_PEOPLE': 10,
    'NUM_GROUPS': 1,
    'AZMAPS_KEY': '',
    'PEOPLE_FILE': './out/people.json',
    'GROUPS_FILE': './out/groups.json',
    'WAYPOINTS_FILE': './out/waypoints.json',
    'TELEMETRY_FILE': './out/telemetry.csv',
    'ROUTES_FILE': './out/routes.json',
    'SIGNALS_FILE': './out/signals.csv',
    'SIGNALS_STORY_FILE': './stories/signals.json',
    'PEOPLE_STORY_FILE': './stories/people.json',
    'GROUP_SIZE_MIN': 3,
    'GROUP_SIZE_MAX': 6,
    'DEVICES_MIN':1,
    'DEVICES_MAX':6,
    'KNOWN_WIFI_MIN':3,
    'KNOWN_WIFI_MAX':20
}

CONFIG = {key: type(DEFAULT_CONFIG[key])(os.environ[key]) if key in os.environ else DEFAULT_CONFIG[key] for key in DEFAULT_CONFIG}
