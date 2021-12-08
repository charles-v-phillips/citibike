import os
import pandas
import re

os.chdir('./NYC_Raw_Bike_Share_Data')
for d in os.listdir('.'):
	if re.match('^[0-9]*-[0-9]*',d):
		for f in os.listdir(d):
			print(f)
			print(f'{os.getcwd()}/{d}/{f}')
			os.rename(f'{os.getcwd()}/{d}/{f}',f'{os.getcwd()}/{f}_{d}')
