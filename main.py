import logging

import report
import stock_price

# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def run():
    loader = stock_price.StockData
    data = loader.fetch_history_stock_price_VN('E1VFVN30', '2021-01-01', '2021-10-10')
    logging.info(data)

    finance_report = report.FinanceReport('VND', '2018-01-01', '2021-10-10')
    financial_report = finance_report.get_basic_index()
    logging.info(financial_report)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
