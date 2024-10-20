""" Module for calculating covariance estimates """
import pandas as pd


def sample_cov(returns: pd.DataFrame) -> pd.DataFrame:
    return returns.cov()


def exponential_weight_cov(returns: pd.DataFrame, alpha: float) -> pd.DataFrame:
    # todo
    return


def shrinkage_cov():
    # todo
    return
