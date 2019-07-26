# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:34:48 2019

@author: donal
"""
import json
import pandas as pd

with open(r'C:\Users\donal\Documents\livemap_ua\liveuamap_2019-07-23.geojson') as f:
    data = json.load(f)

idx = [50+i for i in range(20)] 
message = [data['features'][i]['properties']['message'] for i in idx]
lon = [data['features'][i]['geometry']['coordinates'][0] for i in idx]
lat = [data['features'][i]['geometry']['coordinates'][0] for i in idx]
color = [data['features'][i]['properties']['marker-color'] for i in idx]
df = pd.DataFrame({'message': message,'lon': lon,'lat': lat, 'color': color})
data['features']
df
# blue = Afghanistan government and NATO allies
# red = pro-communist, socialist groups
# green = Taliban
# gray = Islamic State
