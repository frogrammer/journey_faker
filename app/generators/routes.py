# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import json
from app.helpers import config, spatial

OUTPUT_FILE = config.CONFIG['ROUTES_FILE']
GROUPS_FILE = config.CONFIG['GROUPS_FILE']

groups = []
with open(GROUPS_FILE, 'r', encoding='UTF-8') as jf:
    groups = json.loads(jf.read())

travel_plans = []

for g in groups:
    routes = spatial.get_route_batch([p['waypoints'] for p in g['members']])
    for i, p in enumerate(g['members']):
        p['route'] = routes[i]
    group_travel_plans = spatial.simulate_group_travel(g)
    for p in g['members']:
        del p['route']
    travel_plans = travel_plans + [group_travel_plans]

with open(OUTPUT_FILE, 'w', encoding='UTF-8') as rf:
    rf.write(json.dumps(travel_plans))
