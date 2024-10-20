import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from backtesting import backtest
from optimizers import ew, gmv

port_opt = {"Equal weight": ew, "Global minimum variance": gmv}

rets_df = pd.read_csv('data/ind30_m_vw_rets.csv', index_col=0) / 100
rets_df.index = pd.to_datetime(rets_df.index, format="%Y%m")

with st.sidebar:
    st.title("Portopt")
    st.text("Portfolio optimization tool")

    assets = st.multiselect("Pick assets to include in the portfolio", rets_df.columns)
    method = st.selectbox("Pick portfolio construction method", port_opt.keys())
    rebalance = st.number_input("Rebalancing frequency (months)", value=1)
    est = st.number_input("Time span used to estimate parameters (months)", value=12)


compute_backtest = st.sidebar.button('Compute')

c1 = st.container()
c1.header("Equity curve")
c2 = st.container()
c2.header("Metrics")

if compute_backtest:
    selected_asset_rets = rets_df[assets]
    backtest_results = backtest(selected_asset_rets, est, port_opt[method], rebalance)
    cumulative_return = (1 + backtest_results).cumprod()

    fig = plt.figure(figsize=(15, 6))
    sns.lineplot(x=backtest_results.index, y=cumulative_return).set(xlabel='common xlabel', ylabel='common ylabel')
    fig.suptitle('Some title')

    c1.pyplot(fig)

    metrics = pd.DataFrame()    # todo
    c2.table(metrics)
