import numpy as np
import pandas as pd

def rsi_wilder(close: pd.Series, period: int = 14) -> pd.Series:
    close = close.astype(float)
    result = pd.Series(np.nan, index=close.index, dtype=float)
    if len(close) <= period:
        return result
    delta = close.diff()
    gains = delta.clip(lower=0)
    losses = -delta.clip(upper=0)
    avg_gain = gains.iloc[1:period + 1].mean()
    avg_loss = losses.iloc[1:period + 1].mean()
    def value(g, l):
        if l == 0:
            return 100.0 if g > 0 else 50.0
        return 100 - 100 / (1 + g / l)
    result.iloc[period] = value(avg_gain, avg_loss)
    for i in range(period + 1, len(close)):
        avg_gain = (avg_gain * (period - 1) + gains.iloc[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses.iloc[i]) / period
        result.iloc[i] = value(avg_gain, avg_loss)
    return result

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['SMA_20'] = df['Close'].rolling(20, min_periods=20).mean()
    df['SMA_50'] = df['Close'].rolling(50, min_periods=50).mean()
    df['RSI_14'] = rsi_wilder(df['Close'])
    return df
