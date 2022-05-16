import yfinance as yf
import streamlit as st
import datetime
import pandas_datareader as pdr
import cufflinks as cf

st.title("""
Stock Price App 
""")

st.sidebar.header('User Input Features')

Tickers = ['TWTR','GOOGL','NKE','AAPL','AMD','NVDA','FB', 'AMZN','NFLX','MSFT']
ticker = st.sidebar.selectbox('Select ticker', sorted(Tickers), index=0)

start_date = st.sidebar.date_input('Start date', datetime.datetime(2021, 1, 1))
end_date = st.sidebar.date_input('End date', datetime.datetime.now().date())

df_ticker = pdr.DataReader(ticker, 'yahoo', start_date, end_date)

st.header(f'{ticker} Stock Price')

# Create candlestick chart 
qf = cf.QuantFig(df_ticker,name=ticker)

# Bollinger Bands 
qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)

#Moving Average Convergence Divergence
qf.add_macd()

fig = qf.iplot(asFigure=True, dimensions=(700, 500))

# Render plot using plotly_chart
st.plotly_chart(fig)


st.write("""Open Price""")
st.line_chart(df_ticker.Open)

st.write("""Closing Price""")
st.line_chart(df_ticker.Close)


st.write("""High Price""")
st.line_chart(df_ticker.High)

st.write("""Low Price""")
st.line_chart(df_ticker.Low)


st.write("""Volume Price""")
st.line_chart(df_ticker.Volume)






