# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import json
import pandas as pd
from app.helpers import config, spatial

ROUTES_FILE = config.CONFIG['ROUTES_FILE']
OUTPUT_FILE = config.CONFIG['TELEMETRY_FILE']

groups = []
telemetry = []
with open(ROUTES_FILE, 'r', encoding='UTF-8') as jf:
    groups = json.loads(jf.read())

telemetry = [{'id': p['id'], 'name': p['name'], 'lat': t[0], 'lng': t[1], 'time': t[2]} for g in groups for p in g['members'] for t in p['travel_plan']]
telemetry_df = pd.DataFrame(telemetry)
telemetry_df = telemetry_df.sort_values('time')
telemetry_df.to_csv(OUTPUT_FILE, header=True, index=False)