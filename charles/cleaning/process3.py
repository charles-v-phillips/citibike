import os
import pandas as pd
import numpy as np
os.chdir('./parqueted')

for i,f in enumerate(sorted(os.listdir('.'))):
	data = pd.read_parquet(f)
	print(i,f,*data.dtypes)
	
