import numpy as np
import pandas as pd

def add_risk_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Daily_Return'] = df['Close'].pct_change() * 100
    df['Cumulative_Return'] = (df['Close'] / df['Close'].iloc[0] - 1) * 100
    df['Drawdown'] = (df['Close'] / df['Close'].cummax() - 1) * 100
    return df

def risk_summary(df: pd.DataFrame) -> dict:
    returns = df['Close'].pct_change().dropna()
    return {
        'cumulative_return': (df['Close'].iloc[-1] / df['Close'].iloc[0] - 1) * 100,
        'annualized_volatility': returns.std(ddof=1) * np.sqrt(252) * 100 if len(returns) > 1 else float('nan'),
        'maximum_drawdown': (df['Close'] / df['Close'].cummax() - 1).min() * 100,
    }
