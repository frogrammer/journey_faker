# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import aiohttp
from . import config

AZURE_MAPS_KEY = config.CONFIG['AZMAPS_KEY']
POI_SEARCH_STRING = 'https://atlas.microsoft.com/search/poi/json?api-version=1.0&subscription-key={0}&lat={1}&lon={2}&radius={3}&query=cafe'
ROUTE_SEARCH_STRING = 'https://atlas.microsoft.com/route/directions/json?subscription-key={0}&api-version=1.0&query={1}'
POI_SEARCH_RADIUS_M = 1000

async def find_poi(lat: float, lng: float) -> list:
    http_session = aiohttp.ClientSession()
    poi_search = POI_SEARCH_STRING.format(AZURE_MAPS_KEY, lat, lng, POI_SEARCH_RADIUS_M)
    resp = await http_session.get(poi_search)
    data = await resp.json()
    return data

async def find_routes(waypoints: list[list[float]]) -> list:
    http_session = aiohttp.ClientSession()
    waypoint_str = ':'.join(f'{ll[0]},{ll[1]}' for ll in waypoints)
    route_search = ROUTE_SEARCH_STRING.format(AZURE_MAPS_KEY, waypoint_str)
    resp = await http_session.get(route_search)
    data = await resp.json()
    try:
        return data['routes']
    except:
        return [-1]
