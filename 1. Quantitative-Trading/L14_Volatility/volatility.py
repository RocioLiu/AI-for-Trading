import pandas as pd
import numpy as np


def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.

    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']

    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    tickers = prices.ticker.unique()
    volatility = {}

    for i in tickers:
        volatility[i] = (prices.loc[prices['ticker'] == i, 'price']).std()

    most_vol_ticker = max(volatility, key=volatility.get)

    return most_vol_ticker


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
