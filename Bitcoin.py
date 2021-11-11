import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
import streamlit as st
import pandas as pd
import numpy as np

from datetime import date
today = date.today().strftime('%d/%m/%Y')

import  investpy
data = investpy.get_crypto_historical_data(crypto='bitcoin', from_date='1/10/2021', to_date=today)

data2=data.iloc[:,3]


#data = investpy.get_crypto_recent_data(crypto='bitcoin')['Close']
 
#df=pd.read_excel(r'C:\Users\Korisnik\Desktop\SVE\app\Bitcoin.xlsx' ) 

st.bar_chart(data2)