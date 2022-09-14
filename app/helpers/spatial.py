# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import asyncio
import math
import random
import haversine
from . import azmaps, config

centre_latlng = (config.CONFIG['CENTRE_LAT'], config.CONFIG['CENTRE_LNG'])
radius = config.CONFIG['RADIUS_KM']

def get_random_latlng():
    random_latlng = haversine.inverse_haversine(centre_latlng, random.random() * radius,  random.random() * 2 * math.pi)
    verified_position = asyncio.run(azmaps.find_poi(*random_latlng))['results'][0]['position']
    return [verified_position['lat'], verified_position['lon']]

def get_random_latlng_batch(batch_size:float=1):
    random_latlngs = [haversine.inverse_haversine(centre_latlng, random.random() * radius,  random.random() * 2 * math.pi) for i in range(0, batch_size)]
    loop = asyncio.get_event_loop()
    verified_pois =loop.run_until_complete(asyncio.gather(*[azmaps.find_poi(*ll) for ll in random_latlngs]))
    verified_positions = [[poi['results'][0]['position']['lat'], poi['results'][0]['position']['lon']] for poi in verified_pois]
    return verified_positions

def get_route(waypoints: list[list[float]]):
    routes = asyncio.run(azmaps.find_routes(waypoints))
    return routes

def get_route_batch(src_latlng: list[float], dst_latlng: list[float], batch_size: 1):
    return []