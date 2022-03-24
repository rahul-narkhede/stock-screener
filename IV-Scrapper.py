from optionprice import Option
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import requests
import json
import datetime as dt


def get_headers():
    return {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
        "cache-control": "max-age=0",
        "dnt": "1",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}


some_option = Option(european=True,
                     kind='put',
                     s0=416.25,
                     k=415,
                     sigma=0.4008,
                     r=0.018720,
                     start='2022-03-08',
                     end='2022-03-11',
                     dv=0)
print(some_option)
print('------------------------------------------------')
print(some_option.getPrice())

# exp_date = round((dt.datetime(2022, 3, 11, tzinfo=dt.timezone.utc)).timestamp())
date = dt.datetime.strptime('2022-03-11', '%Y-%m-%d')
exp_date = round(dt.datetime(date.year, date.month, date.day, tzinfo=dt.timezone.utc).timestamp())
url = f"https://query1.finance.yahoo.com/v7/finance/options/spy?date={exp_date}"
print(url)
print(f"Back date = {dt.datetime.fromtimestamp(exp_date, tz=dt.timezone.utc).strftime('%Y-%m-%d')}")
response = requests.get(url, headers=get_headers())
print(response.text)
for expiration_date in response.json()['optionChain']['result'][0]['expirationDates']:
    print(
        f"original = {expiration_date} Back date = {dt.datetime.fromtimestamp(expiration_date, tz=dt.timezone.utc).strftime('%Y-%m-%d')}")
put_list = response.json()['optionChain']['result'][0]['options'][0]['puts']
put_option = [x for x in put_list if x['strike'] == 415]
print(json.dumps(put_option, indent=4, sort_keys=True))
# SPY.get_put_data(month =2 , year = 2021)
