import os
import pandas as pd
import numpy as np

path = './NYC'
files = os.listdir(path)

os.chdir('./NYC')
for f in sorted(files):
    data = pd.read_csv(f)
    data.columns = list(map(lambda s: s.lower(),list(data.columns)))

    if 'start station id' in data.columns:
        data.drop(['start station id','end station id'],inplace = True, axis = 1)
    else:
        data.drop(['start_station_id','end_station_id'],inplace = True, axis = 1)
    data.to_csv(f'./../droppedcol/{f}')
    print(f)