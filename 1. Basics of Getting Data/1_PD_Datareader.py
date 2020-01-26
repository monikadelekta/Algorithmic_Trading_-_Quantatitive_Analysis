import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like #is_list_like is moved to pandas.api.types
import pandas_datareader.data as pdr  #.data allows you to extract information from Yahoo
import datetime as dt

ticker = 'AMZN'
start_date = dt.date.today() - dt.timedelta(365)
end_date = dt.date.today()

#extract daily data (smallest granuality)
data = pdr.get_data_yahoo(ticker, start_date, end_date)
print(data) #extracts daily data - open, high, adj colse and volume

#get monthly data
data_monthly = pdr.get_data_yahoo(ticker, start_date, end_date, interval = 'm')
print(data_monthly) #returns monthly data



