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
