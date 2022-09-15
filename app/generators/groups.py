# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import json
import random
from ..helpers import config, file, spatial

OUTPUT_FILE = config.CONFIG['GROUPS_FILE']
WAYPOINTS_FILE = config.CONFIG['WAYPOINTS_FILE']
num_groups = config.CONFIG['NUM_GROUPS']
people = file.read_json(WAYPOINTS_FILE)

random_latlngs = spatial.get_random_latlng_batch(num_groups)
random_meeting_places = [{'id': ll[0], 'latlng': ll[1]} for ll in enumerate(random_latlngs)]
groups = []

for i, ll in enumerate(random_meeting_places):
    group_size = random.randint(config.CONFIG['GROUP_SIZE_MIN'], config.CONFIG['GROUP_SIZE_MAX'])
    group_members = random.choices([p for p in people if 'story' not in p], k=group_size)
    groups.append({
        'id': i,
        'meeting_place': ll,
        'members': group_members
    })
    for p in group_members:
        people.remove(p)
        meeting_waypoint = random.randint(0, len(p['waypoints']))
        p['meeting_waypoint'] = meeting_waypoint
        p['waypoints'].insert(meeting_waypoint, ll['latlng'])

groups.append({
    'id': -1,
    'meeting_place': '',
    'members': people
})

with open(OUTPUT_FILE, 'w', encoding='UTF-8') as out_file:
    out_file.write(json.dumps(groups))
