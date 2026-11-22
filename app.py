import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from src.data_loader import load_prices
from src.indicators import add_indicators
from src.risk_metrics import add_risk_columns, risk_summary
from src.comparison import compare_assets

st.set_page_config(page_title='MarketLens', page_icon='📈', layout='wide')
st.title('MarketLens | Financial Market Analysis')
st.caption('Historical market research • Not investment advice • Data may be delayed')

@st.cache_data(ttl=3600, show_spinner=False)
def cached_prices(ticker, period):
    return load_prices(ticker, period)

@st.cache_data(ttl=3600, show_spinner=False)
def cached_comparison(tickers, period):
    return compare_assets(list(tickers), period)

with st.sidebar:
    st.header('Market selection')
    ticker = st.text_input('Ticker', 'RELIANCE.NS', help='Examples: RELIANCE.NS, AAPL, ^GSPC').strip().upper()
    period = st.selectbox('History', ['6mo', '1y', '2y', '5y'], index=1)
    st.caption('Prices are adjusted for corporate actions by the data provider.')

try:
    df = add_risk_columns(add_indicators(cached_prices(ticker, period)))
    metrics = risk_summary(df)
except Exception as exc:
    st.error(f'Could not load stock data: {exc}')
    st.stop()

st.subheader(f'{ticker} — Technical overview')
a, b, c, d = st.columns(4)
a.metric('Latest adjusted close', f'{df.Close.iloc[-1]:,.2f}')
b.metric('Period price return', f'{metrics["cumulative_return"]:.2f}%')
c.metric('Annualized volatility', f'{metrics["annualized_volatility"]:.2f}%')
d.metric('Max drawdown', f'{metrics["maximum_drawdown"]:.2f}%')

fig = go.Figure()
fig.add_trace(go.Candlestick(x=df.index, open=df.Open, high=df.High, low=df.Low, close=df.Close, name='OHLC'))
for key, color in [('SMA_20', '#f59e0b'), ('SMA_50', '#60a5fa')]:
    fig.add_trace(go.Scatter(x=df.index, y=df[key], name=key, line=dict(color=color)))
fig.update_layout(title='Adjusted OHLC and moving averages', xaxis_rangeslider_visible=False, height=500, xaxis_title='Date', yaxis_title='Price')
st.plotly_chart(fig, use_container_width=True)

rsi_fig = go.Figure(go.Scatter(x=df.index, y=df.RSI_14, name='RSI 14'))
rsi_fig.add_hline(y=70, line_dash='dash', line_color='red')
rsi_fig.add_hline(y=30, line_dash='dash', line_color='green')
rsi_fig.update_layout(title='Wilder RSI (14)', yaxis_range=[0,100], height=280)
st.plotly_chart(rsi_fig, use_container_width=True)

left, right = st.columns(2)
with left:
    fig_return = go.Figure(go.Scatter(x=df.index, y=df.Cumulative_Return, name='Return %'))
    fig_return.update_layout(title='Cumulative price return (%)', height=300)
    st.plotly_chart(fig_return, use_container_width=True)
with right:
    fig_drawdown = go.Figure(go.Scatter(x=df.index, y=df.Drawdown, fill='tozeroy', name='Drawdown %'))
    fig_drawdown.update_layout(title='Historical closing-price drawdown (%)', height=300)
    st.plotly_chart(fig_drawdown, use_container_width=True)

st.download_button('Download analyzed CSV', df.to_csv().encode('utf-8'), file_name=f'{ticker.replace("^", "")}_analysis.csv', mime='text/csv')

st.divider()
st.subheader('Compare stocks and indices')
comparison_text = st.text_input('Comma-separated tickers', 'RELIANCE.NS, TCS.NS, ^NSEI')
comparison_tickers = tuple(t.strip().upper() for t in comparison_text.split(',') if t.strip())
if st.button('Compare assets'):
    if len(comparison_tickers) < 2:
        st.warning('Enter at least two symbols.')
    elif len(comparison_tickers) > 5:
        st.warning('Compare up to five assets at once.')
    else:
        try:
            normalized, summary = cached_comparison(comparison_tickers, period)
            st.line_chart(normalized, y_label='Indexed price (start = 100)')
            st.caption('Each series starts at 100 on its first available date; differing start dates and missing sessions can affect comparison.')
            st.dataframe(summary.rename(columns={'cumulative_return':'Period return (%)','annualized_volatility':'Annualized volatility (%)','maximum_drawdown':'Max drawdown (%)'}), hide_index=True)
        except Exception as exc:
            st.error(f'Comparison unavailable: {exc}')

st.caption('MarketLens is educational research software. Indicators describe historical prices and do not predict future performance.')
