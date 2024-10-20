""" Module for backtesting portfolio construction strategies """

import pandas as pd
from typing import Callable


def backtest(returns: pd.DataFrame, est_window: int, weight_fct: Callable, rebalancing_freq: int,
             **kwargs) -> pd.Series:
    horizon = len(returns)

    weights = []
    for i in range(horizon - est_window):
        if i % rebalancing_freq == 0:
            window_ret = returns.iloc[i:i + est_window]
            mu = window_ret.mean()
            cov = window_ret.cov()
            w = weight_fct(mu=mu, cov=cov)
            print(w.shape)
            weights.append(w)
        else:
            weights.append(weights[-1])

    weights = pd.DataFrame(weights, index=returns.iloc[est_window:].index, columns=returns.columns)
    returns = (weights * returns).sum(axis="columns", min_count=1)

    return returns
