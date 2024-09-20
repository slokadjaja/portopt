import numpy as np
import cvxpy as cp


def min_vol(mu, cov, target_ret):
    """
    Calculate minimum volatility portfolio given a target return
    :param mu: expected return estimates
    :param cov: covariance matrix estimates
    :param target_ret: target return estimate
    :return: optimal portfolio weights
    """

    w = cp.Variable(len(mu))
    objective = cp.Minimize(cp.quad_form(w, cov))
    constraints = [mu.T @ w == target_ret,
                   np.ones_like(mu) @ w == 1,
                   w >= 0]
    prob = cp.Problem(objective, constraints)
    prob.solve()

    return w.value


def gmv(mu, cov):
    """
    Calculate global minimum volatility portfolio
    :param mu: expected return estimates
    :param cov: covariance matrix estimates
    :return: optimal portfolio weights
    """

    w = cp.Variable(len(mu))
    objective = cp.Minimize(cp.quad_form(w, cov))
    constraints = [np.ones_like(mu) @ w == 1,
                   w >= 0]
    prob = cp.Problem(objective, constraints)
    prob.solve()

    return w.value


def ew():
    """
    Compute equal weighted portfolio
    :return:
    """
    # todo
    return


def cw():
    """
    Compute market cap weighted portfolio
    :return:
    """
    # todo
    return


def risk_parity():
    # todo
    return
