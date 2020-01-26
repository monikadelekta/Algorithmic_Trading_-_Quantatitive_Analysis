# ============================================================================
# Import OHLCV data using yahoofinancials
# Author - Mayank Rasu
# =============================================================================
import pandas as pd, datetime
from yahoofinancials import YahooFinancials

all_tickers = ["AAPL","MSFT","CSCO","AMZN","INTC"]

# extracting stock data (historical close price) for the stocks identified
close_prices = pd.DataFrame()
end_date = (datetime.date.today()).strftime('%Y-%m-%d')
beg_date = (datetime.date.today()-datetime.timedelta(1825)).strftime('%Y-%m-%d')
cp_tickers = all_tickers
attempt = 0
drop = []

while len(cp_tickers) != 0 and attempt <=5:
    print("-----------------")
    print("attempt number ", attempt)
    print("-----------------")
    cp_tickers = [j for j in cp_tickers if j not in drop]
    for i in range(len(cp_tickers)):
        try:
            yahoo_financials = YahooFinancials(cp_tickers[i]) #initiate object for each ticker
            json_obj = yahoo_financials.get_historical_stock_data(beg_date, end_date, "daily")
            ohlv = json_obj[cp_tickers[i]]['prices'] #returns json, to get price access JSON
            temp = pd.DataFrame(ohlv)[["formatted_date", "adjclose"]] #from prices get date and adj close
            temp.set_index("formatted_date", inplace=True) #set index as formatted date
            # some elements are duplicated or dividend information is included
            # use duplicated which returns boolean output to know if a row is duplicated or not
            # ~ will do the inverse, change false values to true and vice versa to keep all rows not duplicated
            temp2 = temp[~temp.index.duplicated(keep='first')]
            close_prices[cp_tickers[i]] = temp2["adjclose"]
            drop.append(cp_tickers[i])
        except:
            print(cp_tickers[i], " :failed to fetch data...retrying")
            continue
    attempt += 1

print(close_prices)