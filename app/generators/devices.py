# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import json
from random import randint
from faker import Faker
from faker_wifi_essid import WifiESSID
from app.helpers import config, spatial

num_devices_min = config.CONFIG['DEVICES_MIN']
num_devices_max = config.CONFIG['DEVICES_MAX']
known_wifi_min = config.CONFIG['KNOWN_WIFI_MIN']
known_wifi_max = config.CONFIG['KNOWN_WIFI_MAX']

faker = Faker()
faker.add_provider(WifiESSID)

def generate_devices():
    return [faker.mac_address() for i in range(0, randint(num_devices_min, num_devices_max))]

def generate_known_wifi():
    return [faker.wifi_essid() for i in range(0, randint(known_wifi_min, known_wifi_max))]