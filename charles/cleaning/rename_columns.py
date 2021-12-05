import os
import pandas as pd
import numpy as np



new_columns = {
    'tripduration'              : 'trip_duration',
    'trip duration'             : 'trip_duration',
    'starttime'                 : 'started_at',
    'start time'                : 'started_at',
    'stoptime'                  : 'ended_at',
    'stop time'                 : 'ended_at',
    'start station id'          : 'start_station_id',
    'start station name'        : 'start_station_name',
    'start station latitude'    : 'start_lat',
    'start station longitude'   : 'start_lon',
    'end station id'            : 'end_station_id',
    'end station name'          : 'end_station_name',
    'end station latitude'      : 'end_lat',
    'end station longitude'     : 'end_lon',
    'bikeid'                    : 'bike_id',
    'bike id'                    : 'bike_id',
    'usertype'                 : 'user_type',
    'user type'                 : 'user_type',
    'birth year'                : 'birth_year'

}   

os.chdir('./old_parqueted_files')

for i,f in enumerate(sorted(os.listdir('.'))):
    
    data = pd.read_parquet(f)
    data.columns = list(map(lambda s: s.lower(),list(data.columns)))
    data.rename(columns = new_columns, inplace = True)
    data.to_parquet(f,index = False)
    print(i,f,*data.columns)
    

