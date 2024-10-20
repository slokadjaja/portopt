import numpy as np
import cvxpy as cp
from utils import *
from scipy.optimize import minimize


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


def gmv(mu, cov) -> np.ndarray:
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


def msr(mu, cov, riskfree_rate):
    """
    Returns the weights of the portfolio that gives you the maximum sharpe ratio
    given the riskfree rate and expected returns and a covariance matrix
    """
    n = mu.shape[0]
    init_guess = np.repeat(1 / n, n)
    bounds = ((0.0, 1.0),) * n  # an N-tuple of 2-tuples!
    # construct the constraints
    weights_sum_to_1 = {'type': 'eq',
                        'fun': lambda weights: np.sum(weights) - 1
                        }

    def neg_sharpe(weights, riskfree_rate, er, cov):
        """
        Returns the negative of the sharpe ratio
        of the given portfolio
        """
        r = portfolio_return(weights, er)
        vol = portfolio_vol(weights, cov)
        return -(r - riskfree_rate) / vol

    weights = minimize(neg_sharpe, init_guess,
                       args=(riskfree_rate, mu, cov), method='SLSQP',
                       options={'disp': False},
                       constraints=(weights_sum_to_1,),
                       bounds=bounds)
    return weights.x


def ew(mu, cov) -> np.ndarray:
    """
    Compute equal weighted portfolio
    :return:
    """
    return np.array([1/len(mu) for i in range(len(mu))])


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
