import os
import pandas as pd
import numpy as np

# os.chdir('./droppedcol')

# for i,f in enumerate(sorted(os.listdir('.'))):
	
# 	data = pd.read_csv(f)
# 	f = f.replace('.csv','')
# 	data.to_parquet(f'./../parquet/{f}.parquet')
# 	print(i,f)

os.chdir('./parquet')

sumrow = 0
sumnull = 0

for f in sorted(os.listdir('.')):
	data = pd.read_parquet(f)
	sumrow += len(data)
	sumnull += data.isnull().sum().sum()
	print(f'{f} : {len(data)}')
	print(data.isnull().sum().sum())
	print()

print(f'# of rows in total: {sumrow}')
print(f'# of nulls in total: {sumnull}')

