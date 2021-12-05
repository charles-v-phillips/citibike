import os
import pandas as pd
import numpy as np

os.chdir('./droppedcol')

# for i, f in enumerate(sorted(os.listdir('.'))):
# 	df = pd.read_csv(f)
# 	df.drop(['unnamed: 0'], axis = 1, inplace = True)
# 	df.to_csv(f'./{f}', index = False)
# 	print(i, f)

# sum = 0
# for f in sorted(os.listdir('.')):
# 	data = pd.read_csv(f)
# 	print(f'{f} : {len(data)}')
# 	sum += len(data)
# print(f'FINAL SUM : {sum}')

sumrow = 0
sumnull = 0

for f in sorted(os.listdir('.')):
	data = pd.read_csv(f)
	sumrow += len(data)
	sumnull += data.isnull().sum().sum()
	print(f'{f} : {len(data)}')
	print(data.isnull().sum().sum())
	print()

print(f'# of rows in total: {sumrow}')
print(f'# of nulls in total: {sumnull}')