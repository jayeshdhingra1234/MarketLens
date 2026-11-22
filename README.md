# MarketLens — Financial Market Analysis Dashboard

**A Python-based financial market research and technical analysis project**

MarketLens is a financial analytics project focused on analyzing historical stock prices, identifying market trends, and evaluating investment risk through quantitative techniques.

The project combines financial market concepts with Python programming, statistical analysis, and data visualization to make historical market behavior easier to study.

## Features

The project is organized around the following analytical components:

- **Market Data Analysis:** Historical stock prices, trading volumes, and price movements.
- **Technical Indicators:** Simple Moving Averages (SMA), Relative Strength Index (RSI), and trend analysis.
- **Financial Visualization:** Price charts, candlestick charts, and indicator visualizations.
- **Return Analysis:** Daily returns and cumulative performance.
- **Risk Analysis:** Historical volatility and drawdown calculations.
- **Asset Comparison:** Comparative analysis of multiple stocks and market indices.

**Development status:** Initial implementation in progress. Features will be marked as completed after testing.

## Technology Stack

| Technology | Application |
|---|---|
| Python | Financial calculations and data processing |
| Pandas | Data manipulation |
| NumPy | Numerical analysis |
| yfinance | Historical financial data |
| Matplotlib | Statistical visualization |
| Plotly | Interactive financial charts |
| Google Colab | Development environment |
| Streamlit | Dashboard interface |

## Project Architecture

```text
MarketLens/
├── README.md
├── requirements.txt
├── notebooks/
│   └── market_analysis.ipynb
├── src/
│   ├── data_loader.py
│   ├── technical_indicators.py
│   └── risk_metrics.py
├── outputs/
│   └── charts/
└── tests/
```

## Installation

The project uses Python 3 and commonly available financial data analysis libraries.

```bash
git clone https://github.com/jayeshdhingra1234/MarketLens.git
cd MarketLens
pip install pandas numpy yfinance matplotlib plotly streamlit
```

The application entry point and run commands will be documented after implementation.

## Analysis Methodology

### 1. Historical Market Data

MarketLens uses historical Open, High, Low, Close, and Volume (OHLCV) data as the foundation for financial analysis.

### 2. Technical Analysis

The analytical approach includes:

- 20-day Simple Moving Average
- 50-day Simple Moving Average
- 14-period Relative Strength Index
- Price momentum and trend interpretation

### 3. Quantitative Risk Analysis

The project examines:

- Percentage returns
- Historical volatility
- Maximum drawdown
- Comparative asset performance

### 4. Financial Market Research

MarketLens is designed to support research into stock price behavior, market trends, and the relationship between returns and risk.

## Future Enhancements

- Fundamental analysis using financial statements
- International market indices
- Currency and commodity analysis
- Futures market data integration
- Portfolio performance analytics
- Interactive Streamlit dashboard

## Project Purpose

MarketLens was initiated to explore the practical application of programming, mathematics, and financial market analysis.

The project reflects an interest in technical analysis, quantitative research, financial markets, and data-driven decision-making.

## Disclaimer

This project is intended for educational and research purposes only. It does not provide financial advice or guarantee the accuracy of market forecasts.

