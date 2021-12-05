import os

path = './NYC'
files = os.listdir(path)

os.chdir('./NYC')
for f in sorted(files):
	os.rename(f, f.replace("citibike-tripdata", "data"))
	os.rename(f, f.replace(" Citi Bike trip data", "data"))
	os.rename(f, f.replace(" ", ""))
	if f[4] != '-':
	 	os.rename(f, f[:4] + "-" + f[4:])
	print(f)