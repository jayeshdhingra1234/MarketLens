import pandas as pd
import yfinance as yf

COLUMNS = ['Open', 'High', 'Low', 'Close', 'Volume']

def load_prices(ticker: str, period: str = '1y') -> pd.DataFrame:
    ticker = ticker.strip().upper()
    if not ticker:
        raise ValueError('Ticker is required')
    df = yf.Ticker(ticker).history(period=period, interval='1d', auto_adjust=True)
    if df.empty:
        raise ValueError(f'No historical prices found for {ticker}')
    df = df[COLUMNS].dropna(subset=['Close']).copy()
    if df.empty:
        raise ValueError(f'No valid closing prices for {ticker}')
    return df
