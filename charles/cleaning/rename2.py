import os
os.chdir('NYC_Raw_Bike_Share_Data')
for f in os.listdir():
	os.rename(f,f.replace('.csv','')+ '.csv')
