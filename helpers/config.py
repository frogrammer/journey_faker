import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_CONFIG = {
    'CENTRE_LAT':0.0,
    'CENTRE_LNG':0.0,
    'RADIUS_KM': 5,
    'NUM_JOURNEYS': 10,
    'NUM_PEOPLE': 10,
    'NUM_MEETING_POIS': 1,
    'AZMAPS_KEY': ''
}

CONFIG = {key: type(DEFAULT_CONFIG[key])(os.environ[key]) if key in os.environ else DEFAULT_CONFIG[key] for key in DEFAULT_CONFIG}
