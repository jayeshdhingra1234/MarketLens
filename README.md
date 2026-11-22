MarketLens — Financial Market Analysis Dashboard
A Python/Streamlit dashboard for historical OHLCV stock data, technical indicators and quantitative risk analysis.
Features
Historical adjusted OHLCV data via yfinance
20- and 50-session simple moving averages; 14-period Wilder RSI
Interactive Plotly candlestick and indicator charts
Daily and cumulative price returns, annualized historical volatility, and maximum closing-price drawdown
Comparison of up to five stocks or indices using normalized historical prices and risk metrics
Downloadable CSV analysis
Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Deploy on Streamlit Community Cloud
Connect your GitHub repository, select branch `main`, and set the entrypoint to `app.py`. Installations use `requirements.txt`.
Structure
`app.py` — Streamlit UI and charts
`src/data_loader.py` — market data retrieval
`src/indicators.py` — SMA and RSI
`src/risk_metrics.py` — returns, volatility and drawdown
`src/comparison.py` — multi-asset comparison
`tests/test_calculations.py` — synthetic-data unit tests
Tests
```bash
python -m unittest discover -s tests -v
```
Limitations
Uses external Yahoo Finance historical data, which may be unavailable or delayed. Adjusted prices and differing market calendars can affect comparisons. This is not a live trading or prediction system. No investment recommendations are provided.
Author
Jayesh Dhingra — B.Tech CSE (AI & ML), VIT Bhopal University.
