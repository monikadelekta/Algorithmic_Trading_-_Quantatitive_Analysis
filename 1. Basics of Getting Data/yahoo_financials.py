#extracts data through webscraping and not an API
from yahoofinancials import YahooFinancials #https://github.com/JECSand/yahoofinancials

ticker = 'AMZN'
yahoo_financials = YahooFinancials(ticker) #new object
historic_stock_prices = yahoo_financials.get_historical_stock_data('2018-01-26', '2019-01-26', 'daily')

print(historic_stock_prices)





