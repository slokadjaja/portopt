### Portfolio optimization tool

The Portfolio Optimization Tool helps investors create efficient portfolios by maximizing returns and 
minimizing risks. It uses modern portfolio theory (MPT) and supports several optimization strategies, 
including mean-variance optimization. It's designed for both backtesting and portfolio construction, 
allowing users to export optimized portfolios in various formats for further analysis.

To run frontend, run ```streamlit run frontend.py```

#### Todos

- Data source: yfinance or alphavantage? currently only using fama-french industry portfolio returns
- Docstrings with type hints
- Add metrics
- Use sql database to store asset data
- Improve backtest plot, show metrics on dashboard