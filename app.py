import yfinance as yf
import streamlit as st
st.write("""
##  Stock closing price""")
tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerSymbol2 = 'EBAY'
tickerData2 = yf.Ticker(tickerSymbol2)
from datetime import date
today = date.today().strftime('%Y-%m-%d')
tickerDf  = tickerData.history(period='1d', start='2021-1-1', end=today)
tickerDf2 = tickerData2.history(period='1d', start='2021-1-1', end=today)
st.write("""
Tesla
""")
st.line_chart(tickerDf.Close)
st.write("""
eBay
""")
st.line_chart(tickerDf2.Close)