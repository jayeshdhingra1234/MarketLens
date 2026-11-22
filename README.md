
# MarketLens — Financial Market Analysis Dashboard

A Python and Streamlit application for analyzing historical stock market data, technical indicators, and quantitative risk.


## Live Dashboard

🚀 **Try MarketLens Online**

[Open MarketLens Financial Analysis Dashboard](https://marketlens-jayesh.streamlit.app/)

Explore historical stock prices, technical indicators,
risk metrics, and multiple-stock comparisons.

## Overview

MarketLens combines Python programming with financial market analysis. It retrieves historical OHLCV data, calculates technical indicators, measures investment risk, and visualizes historical stock performance.

The project is designed for educational financial research.

## Features

### 1. Historical Market Data
- Retrieves stock data using yfinance.
- Processes Open, High, Low, Close, and Volume data.
- Supports historical stock market analysis.

### 2. Technical Analysis
- 20-day Simple Moving Average (SMA 20).
- 50-day Simple Moving Average (SMA 50).
- 14-period Relative Strength Index (RSI).
- Interactive candlestick charts.
- Moving-average and momentum visualization.

### 3. Quantitative Risk Analysis
- Daily percentage returns.
- Cumulative price returns.
- Annualized historical volatility.
- Maximum historical drawdown.

### 4. Multiple Stock Comparison
- Compare up to five stocks or indices.
- View normalized historical price performance.
- Examine historical return and risk metrics.

### 5. Interactive Dashboard
- Streamlit-based user interface.
- Stock ticker selection.
- Interactive Plotly charts.
- Downloadable CSV analysis results.

## Technologies Used

- Python
- Pandas
- NumPy
- yfinance
- Matplotlib
- Plotly
- Streamlit

## Project Structure

```text
MarketLens/
├── app.py
├── README.md
├── requirements.txt
├── notebooks/
├── outputs/
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── indicators.py
│   ├── risk_metrics.py
│   └── comparison.py
└── tests/
    └── test_calculations.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/jayeshdhingra1234/MarketLens.git
cd MarketLens
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Launch the dashboard:

```bash
streamlit run app.py
```

## Running on Streamlit Community Cloud

1. Sign in at https://share.streamlit.io/
2. Connect your GitHub account.
3. Select the MarketLens repository.
4. Choose the main branch.
5. Set the application file to `app.py`.
6. Deploy the application.

## Testing

Run the calculation tests:

```bash
python -m unittest discover -s tests -v
```

## Future Improvements

- Fundamental analysis using financial statements.
- International futures and commodity market analysis.
- Portfolio risk analytics.
- Additional quantitative indicators.

## Limitations

- Market data depends on Yahoo Finance availability.
- Historical indicators cannot guarantee future performance.
- The application does not execute trades.
- This project is intended for educational research, not investment advice.

## Author

**Jayesh Dhingra**

B.Tech Computer Science and Engineering (AI & ML)

VIT Bhopal University | Graduation: 2028


