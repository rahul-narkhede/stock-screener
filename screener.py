from sklearn.linear_model import LinearRegression

from pandas_datareader import data as pdr
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
import datetime
import time
from tabulate import tabulate
import numpy as np
import requests

# yf.pdr_override()
# tickers = si.tickers_sp500()
# start_date = datetime.datetime.now() - datetime.timedelta(days=365 * 5)
# end_date = datetime.date.today()
# tickers.append('^GSPC')
# # Index Returns
# # index_df = pdr.get_data_yahoo('SPY', start_date, end_date)
# # index_df['Percent Change'] = index_df['Adj Close'].pct_change()
# # index_return = round((index_df['Percent Change'] + 1).cumprod(), 2)
# stock = []
# stock_return = []
# beta = []
# ex_dividend_date = []
# indexx = 0
# stock_df = pdr.get_data_yahoo(tickers, start_date, end_date)['Adj Close']
#
# start = '2019-10-1'
# end = '2022-02-23'
#
#
# for ticker in tickers:
#     print(f'Fetching for Ticker {ticker}')
#     percent_change = stock_df[ticker].pct_change()
#     return_on_stock = round((percent_change + 1).cumprod()[-1], 2)
#     stock_return.append(return_on_stock)
#
#     stock_data = yf.Ticker(ticker)
#     # for k, v in apple.info.items():
#     #     print(f'{k}: {v}')
#     if stock_data.info['exDividendDate'] is not None:
#         ex_dividend_date.append(datetime.datetime.fromtimestamp(stock_data.info['exDividendDate']))
#     else:
#         ex_dividend_date.append(None)
#     beta.append(stock_data.info['beta'])
#     time.sleep(15)
#
# data = pd.Dataframe({'Stock': stock,
#                      'Return': stock_return,
#                      'beta': beta,
#                      'ex_dividend_date': ex_dividend_date})
# print(tabulate(data, headers='keys', tablefmt='psql'))

other_details_json_link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{" \
                          "0}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData" \
                          "%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics" \
                          "%2CcalendarEvents&corsDomain=finance.yahoo.com".format('AAPL')
summary_json_response = requests.get(other_details_json_link)
print(summary_json_response.text)
