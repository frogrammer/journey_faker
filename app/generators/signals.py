# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import random
import geopandas as gpd
import pandas as pd
from app.helpers import config, file, spatial

ROUTES_FILE = config.CONFIG['ROUTES_FILE']
SIGNALS_STORY_FILE = config.CONFIG['SIGNALS_STORY_FILE']
OUTPUT_FILE = config.CONFIG['SIGNALS_FILE']

signals_story = file.read_json(SIGNALS_STORY_FILE)
groups = file.read_json(ROUTES_FILE)
signals = [{'lat': t[0], 'lng': t[1], 'time': t[2], 'devices': p['devices'], 'known_wifi': p['known_wifi']} for g in groups for p in g['members'] for t in p['travel_plan'] if p['id'] in signals_story['signals_from']]
recipient = [p for g in groups for p in g['members'] if p['id'] == signals_story['person_id']][0]

signals_df = pd.DataFrame(signals)
signals_df['distance'] = signals_df.apply(lambda row: spatial.calculate_distance_from_person(recipient, row['lat'], row['lng'], row['time']), axis=1)
signals_df['signal_strength'] = signals_df['distance'].apply(spatial.simulate_signal_strength)
signals_df['source'] = signals_df['devices'].apply(random.choice)
signals_df['wifi_ssid'] = signals_df['known_wifi'].apply(random.choice)
signals_df = signals_df.drop(columns=['known_wifi', 'devices', 'lat', 'lng']).sort_values('time')
signals_df[signals_df['signal_strength'].notna()].to_csv(OUTPUT_FILE, header=True, index=False)