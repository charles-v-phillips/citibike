import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2018, 12, 31)

df = web.get_data_yahoo('stock',start,end)

print(df.head())