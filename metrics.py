import pandas as pd


def drawdown(prices: pd.DataFrame):
    """
    Calculate drawdown based on prices
    :param prices: DataFrame containing asset prices
    :return: drawdown dataframe
    """
    return (prices - prices.cummax()) / prices.cummax()


def sharpe(returns: pd.DataFrame):
    # todo
    return


def kurtosis(returns: pd.DataFrame):
    kurtosis = ((returns - returns.mean()) ** 4).mean() / (returns.std(ddof=0) ** 4)
    return kurtosis


def skewness(returns: pd.DataFrame):
    skew = ((returns - returns.mean()) ** 3).mean() / (returns.std(ddof=0) ** 3)
    return skew
