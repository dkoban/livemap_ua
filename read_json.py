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

import requests

# api-endpoint 
#https://me.liveuamap.com/promo/api
#r=1000&lat=37.2965314&lng=-122.0976092

URL = 'https://a.liveuamap.com/api?a=mpts&res=56&time=1564107271&count=3&key=2b44aa24e6051d8fe8c37e789007c2f0'

# sending get request and saving the response as response object 
r = requests.get(url = URL)

# extracting data in json format 
data = r.json() 
data['fields'][0]['name']
 #{
 #      	"key": "cf1ea9d1bc6d89d831a1aa85b6beef56",
 #      	"last": 0,
 #      	"venues": [{
 #      		"videocode": "",
 #      		"videotype": null,
 #      		"resid": 3,
 #      		"name": "#Raqqa Coalition Warplanes targeted a checkpoint for #ISIS near the old bridge today at 01:30 AM #Syria #ISIS ",
 #      		"video": "",
 #      		"id": 21289697,
 #      		"time": "2 jaar geleden",
 #      		"pics": [],
 #      		"timestamp": 1449685740,
 #      		"source": "https:\/\/twitter.com\/Raqqa_SL\/status\/674657230604472323",
 #      		"picpath": "https:\/\/a.liveuamap.com\/images\/is14\/bomb_blue.png",
 #      		"status_id": 0,
 #      		"svimg": "bomb-2",
 #      		"resource": 5,
 #      		"type_id": 1,
 #      		"lat": "35.93189",
 #      		"lng": "39.01067",
 #      		"link": "http:\/\/isis.liveuamap.com\/nl\/2015\/9-december-raqqa-coalition-warplanes-targeted-a-checkpoint",
 #      		"picture": "https:\/\/a.liveuamap.com\/pics\/2015\/12\/09\/21289697_0.jpg",
 #      		"city": null,
 #      		"img_share": "",
 #      		"location": null,
 #      		"points": "",
 #      		"viaSource": "Raqqa_SL"
 #      	}],
 #      	"fields": [],
 #      	"kmls": [],
 #      	"datats": 1449686409,
 #      	"datac": "09",
 #      	"datamn": "12",
 #      	"datam": "December",
 #      	"datay": "2015",
 #      	"amount": 1,
 #      	"count": 1,
 #      	"res": [3],
 #      	"center": [{
 #      		"type": "mobile",
 #      		"lat": 35.021,
 #      		"lng": 38.7488,
 #      		"zoom": 6
 #      	}]
 #      }