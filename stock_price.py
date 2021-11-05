import logging as logging
from datetime import datetime

import pandas as pd
import requests

HEADERS = {'content-type': 'application/json', 'User-Agent': 'Mozilla'}


class StockData:
    def fetch_history_stock_price_VN(ticker, start_date, end_date):
        API_VNDIRECT = 'https://finfo-api.vndirect.com.vn/v4/stock_prices/'
        query = 'code:' + ticker + '~date:gte:' + start_date + '~date:lte:' + end_date
        delta = datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')
        params = {
            "sort": "date",
            "size": delta.days + 1,
            "page": 1,
            "q": query
        }
        res = requests.get(API_VNDIRECT, params=params, headers=HEADERS)
        data = res.json()['data']
        convert_data = pd.DataFrame(data)
        return convert_data
