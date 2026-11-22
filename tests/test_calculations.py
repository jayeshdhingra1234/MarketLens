import unittest
import numpy as np
import pandas as pd
from src.indicators import add_indicators, rsi_wilder
from src.risk_metrics import add_risk_columns, risk_summary

class CalculationsTest(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'Close': np.arange(1, 61, dtype=float)})

    def test_sma(self):
        result = add_indicators(self.df)
        self.assertAlmostEqual(result['SMA_20'].iloc[-1], 50.5)
        self.assertAlmostEqual(result['SMA_50'].iloc[-1], 35.5)

    def test_rsi_uptrend(self):
        self.assertAlmostEqual(rsi_wilder(self.df.Close).iloc[-1], 100)

    def test_flat_rsi(self):
        self.assertAlmostEqual(rsi_wilder(pd.Series([5.] * 60)).iloc[-1], 50)

    def test_drawdown(self):
        sample = pd.DataFrame({'Close': [100., 120., 90., 110.]})
        self.assertAlmostEqual(risk_summary(sample)['maximum_drawdown'], -25)
        self.assertAlmostEqual(add_risk_columns(sample)['Daily_Return'].iloc[1], 20)

if __name__ == '__main__':
    unittest.main()
