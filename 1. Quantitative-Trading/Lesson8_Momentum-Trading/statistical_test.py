import pandas as pd
import numpy as np
import scipy.stats as stats


def analyze_returns(net_returns):
    """
    Perform a t-test, with the null hypothesis being that the mean return is zero.

    Parameters
    ----------
    net_returns : Pandas Series
        A Pandas Series for each date

    Returns
    -------
    t_value
        t-statistic from t-test
    p_value
        Corresponding p-value
    """
    # TODO: Perform one-tailed t-test on net_returns
    # Hint: You can use stats.ttest_1samp() to perform the test.
    #       However, this performs a two-tailed t-test.
    #       You'll need to divde the p-value by 2 to get the results of a one-tailed p-value.
    null_hypothesis = 0.0
    t_value, p_value = stats.ttest_1samp(net_returns, null_hypothesis)
    p_value = p_value / 2

    return t_value[0], p_value[0]


def test_run(filename='net_returns.csv'):
    """Test run analyze_returns() with net strategy returns from a file."""
    df = pd.read_csv(filename, header=0)
    net_returns = pd.DataFrame(df.loc[:, df.columns[0]].str.split(',').tolist(), columns=['date', 'returns'])
    net_returns['date'] = pd.to_datetime(net_returns['date'])
    net_returns['returns'] = net_returns['returns'].astype('float')
    net_returns.set_index('date', inplace=True)

    t, p = analyze_returns(net_returns)
    print(f"t-statistic: {t:<.3f}\np-value: {p:<.6f}")


if __name__ == '__main__':
    test_run()






