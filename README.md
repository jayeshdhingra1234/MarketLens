# MarketLens — Financial Market Analysis

**Python-Based Stock Market Technical and Quantitative Analysis**

MarketLens is a Python-based financial market analysis project that retrieves historical stock market data, calculates technical indicators, visualizes price movements, and evaluates historical market risk.

The project combines financial market knowledge with programming, statistics, and data visualization to support educational research into stock market behavior.

## Key Features

### 1. Historical Market Data
- Retrieves historical OHLCV data using `yfinance`.
- Processes stock market data using Pandas.
- Supports analysis of historical daily trading sessions.

### 2. Technical Indicators
- **SMA 20:** 20-session Simple Moving Average.
- **SMA 50:** 50-session Simple Moving Average.
- **RSI 14:** Relative Strength Index calculated using Wilder's smoothing.
- Basic trend and momentum interpretation.

### 3. Financial Data Visualization
- Interactive candlestick charts using Plotly.
- SMA 20 and SMA 50 overlays.
- RSI visualization with reference levels of 30 and 70.
- Cumulative price return and drawdown charts.

### 4. Quantitative Risk Analysis
- Daily percentage returns.
- Cumulative historical price returns.
- Annualized historical volatility.
- Maximum historical closing-price drawdown.

### 5. Exportable Results
- Financial analysis dataset in CSV format.
- Interactive candlestick chart in HTML format.
- Reproducible Google Colab notebook.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Financial data processing |
| NumPy | Numerical calculations |
| yfinance | Historical market data |
| Matplotlib | Data visualization |
| Plotly | Interactive candlestick charts |
| Google Colab | Notebook development and execution |
| GitHub | Version control and project hosting |

## Repository Structure

```text
MarketLens/
├── README.md
├── requirements.txt
├── notebooks/
│   └── MarketLens_Stock_Analysis.ipynb
└── outputs/
    ├── marketlens_full_analysis.csv
    └── marketlens_candlestick_chart.html
```

## Installation and Usage

### Option 1: Google Colab

1. Download `MarketLens_Stock_Analysis.ipynb` from the `notebooks` directory.
2. Open Google Colab.
3. Upload the notebook.
4. Execute the cells sequentially.
5. Review the technical indicators, charts, and risk analysis report.

### Option 2: Local Python Environment

Clone the repository:

```bash
git clone https://github.com/jayeshdhingra1234/MarketLens.git
cd MarketLens
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the notebook in a compatible Jupyter environment and execute its cells.

An internet connection is required to retrieve historical financial data.

## Financial Analysis Methodology

### Simple Moving Average

The SMA measures the average closing price over a selected number of trading sessions.

MarketLens calculates SMA 20 and SMA 50 to examine historical trend direction.

### Relative Strength Index

The 14-period RSI measures the relative strength of recent gains and losses.

Conventional reference levels are:

- Above 70: Overbought zone
- Below 30: Oversold zone
- Between 30 and 70: Intermediate zone

These levels are descriptive indicators, not guaranteed trading signals.

### Historical Volatility

Annualized historical volatility is estimated using the standard deviation of daily returns multiplied by the square root of 252.

### Maximum Drawdown

Maximum drawdown measures the largest decline from a previous closing-price peak within the selected historical period.

## Sample Analysis

The initial implementation analyzes historical daily price data for Reliance Industries (`RELIANCE.NS`).

The notebook produces:

- Technical indicator calculations
- Price and momentum charts
- Historical return measurements
- Volatility and drawdown statistics
- Exportable analysis files

Results depend on the date and market data available when the notebook is executed.

## Future Enhancements

- Fundamental financial statement analysis
- Stock and index comparisons
- International futures and commodities analysis
- Portfolio risk analytics
- Interactive Streamlit dashboard

## Limitations

- Historical price indicators do not predict future returns reliably.
- Market data availability depends on the external data provider.
- Volatility and drawdown calculations describe historical behavior.
- The current version is a notebook-based analytical tool, not a live trading system.
- The project does not execute trades.

## Disclaimer

MarketLens is developed for educational and financial research purposes. It does not provide personalized investment recommendations or guarantee trading profitability.
