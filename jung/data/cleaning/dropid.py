import os
import pandas as pd
import numpy as np
import time
new_columns = {'starttime': 'started_at', 
               'stoptime': 'ended_at',
               'start station name': 'start_station_name',
               'start station latitude': 'start_lat',
               'start station longitude': 'start_lng',
               'end station name': 'end_station_name',
               'end station latitude': 'end_lat',
               'end station longitude': 'end_lng'}


os.chdir('./droppedcol')


for i, f in enumerate(sorted(os.listdir('.'))):
	print(i,f)
	data = pd.read_csv(f)
	data.columns = list(map(lambda s: s.lower(),list(data.columns)))

	data.rename(columns = new_columns, inplace = True)

	data.to_csv(f'./{f}', index = False)