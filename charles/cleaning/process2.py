import os
import pandas as pd

os.chdir('./parqueted')

for i, f in enumerate(sorted(os.listdir('.'))):
	data = pd.read_parquet(f)
	print(i,f,*list(data.columns))
