from alpha_vantage.timeseries import TimeSeries

# used for intraday trading strategies
# API key from alpha vantage website
# https://www.alphavantage.co/documentation/


# supported intervals include 1min, 5min, 15min, 30min, 60min
ts = TimeSeries(key=open('../key.rtf','r').read(), output_format= 'pandas')
data, meta_data = ts.get_intraday(symbol = 'AAPL', interval = '1min', outputsize = 'full')

print(data)
print(meta_data)