import json
from datetime import datetime
from datetime import timedelta

from yahoo_fin import options
from tabulate import tabulate
import pandas_datareader.data as web
import yfinance as yf
import opstrat as op

bsm=op.black_scholes(K=420.08, St=415, r=2.0040002, t=2,
                     v=29.78585839843749, type='p')
print(bsm)
