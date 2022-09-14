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
    return routes[0]

def get_route_batch(waypoints_batch: list[list[list[float]]]):
    loop = asyncio.get_event_loop()
    routes_batch = [r[0] for r in loop.run_until_complete(asyncio.gather(*[azmaps.find_routes(w) for w in waypoints_batch]))]
    return routes_batch

def simulate_group_travel(group: dict):
    for p in group['members']:
        travel_time = 0
        p['travel_plan'] = []
        p['time_at_meeting'] = 0
        if p['route'] != -1:
            for i, leg in enumerate(p['route']['legs']):
                leg_time = leg['summary']['travelTimeInSeconds']
                num_points = len(leg['points'])
                time_per_point = leg_time / num_points
                leg_points = [[p['latitude'], p['longitude'], math.ceil(travel_time + time_per_point * i)] for i, p in enumerate(leg['points'])]
                p['travel_plan'] = p['travel_plan'] + leg_points
                travel_time = travel_time + leg_time
                if group['id'] != -1 and i == p['meeting_waypoint']:
                    p['time_at_meeting'] = travel_time

    if group['id'] != -1:
        max_meeting_time = max([p['time_at_meeting'] for p in group['members']])

        for p in group['members']:
            time_offset = max_meeting_time - p['time_at_meeting']
            p['travel_plan'] = [[t[0], t[1], t[2] + time_offset] for t in p['travel_plan']]

    return group