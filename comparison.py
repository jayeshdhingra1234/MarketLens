import pandas as pd
from .data_loader import load_prices
from .risk_metrics import risk_summary

def compare_assets(tickers: list[str], period: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    normalized = {}
    rows = []
    for ticker in dict.fromkeys(t.strip().upper() for t in tickers if t.strip()):
        prices = load_prices(ticker, period)
        close = prices['Close']
        normalized[ticker] = close / close.iloc[0] * 100
        rows.append({'Ticker': ticker, **risk_summary(prices)})
    if not rows:
        raise ValueError('Enter at least one ticker')
    return pd.DataFrame(normalized), pd.DataFrame(rows)
