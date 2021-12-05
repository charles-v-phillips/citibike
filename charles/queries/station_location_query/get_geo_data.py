import pandas as pd
import geopy
from geopy.geocoders import Nominatim, GoogleV3
from geopy.point import Point
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent = 'fuck_off')

data = pd.read_csv('station_locations.csv')
data.rename(columns={'f0_' : 'lat', 'f1_' : 'lon'},inplace = True)


rv = {}

for i, row in data.iterrows():
	print(f'{i} of {len(data)}')
	addr = geolocator.reverse('{}, {}'.format(row.lat,row.lon)).raw['address']
	rv[row['start_station_id']] = addr

rv = pd.DataFrame.from_dict(rv)

	



rv.to_csv('location_info.csv',index = False)

