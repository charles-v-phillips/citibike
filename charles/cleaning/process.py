import os
import pandas as pd
import glob

os.chdir('./NYC_Raw_Bike_Share_Data')

for i, f in enumerate(sorted(glob.glob('bikeshare*.csv'))):
	print(i,f)
	data = pd.read_csv(f,delimiter = '\t', error_bad_lines = False)
	data.drop(['_lat','_long'],axis = 1, inplace = True)
	for c in ['lat3','dock_name6','dock_name7','_lat3','_long3','avail_bikes3','Unnamed: 0']:
		if c in data.columns:
			data.drop(c, inplace = True, axis = 1)
	
	for c in data.columns:
		if 'MM' in c or 'MN' in c :
			data.drop(c,inplace=True, axis = 1)	
		
	data.drop(data[data['dock_name'].isna()].index,inplace = True)
	data.to_parquet('./../parqueted/' + f.replace('.csv','') + '.parquet')
