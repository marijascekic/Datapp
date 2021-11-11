import yfinance as yf
import streamlit as st
st.write("""
#  Stock closing price of Tesla """)
tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
from datetime import date
today = date.today().strftime('%Y-%m-%d')
tickerDf = tickerData.history(period='1d', start='2021-10-1', end=today)
st.line_chart(tickerDf.Close)