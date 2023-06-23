import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.config import config, LOG
import yahoo_fin.stock_info as si
from utils.yfinance_scraper import get_quote_table, get_stats, get_balance_sheet
from yahoo_fin.news import get_yf_rss
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator, StochRSIIndicator
from streamlit_echarts import st_echarts
import datetime
import json
from utils.indicators import render_indicators
from utils.analyst_info import render_analyst_info
from utils.news import render_news
from utils.quote_table import render_quote_table


###########
# sidebar #
###########

option = st.sidebar.selectbox('Select one symbol', (config.client_portfolio.keys()))
import datetime
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')


###########
# SUMMARY #
###########
# TODO: Create Report Functionality


###########
# COMPANY PERFORMANCE #
###########

render_quote_table(option)

###########
# COMPANY - RELATED NEWS #
###########
# TODO: Combine LLM solution to summarize news ?

render_news(option)


###########
# ANALYSIS #
###########
# TODO: Combine LLM solution to summarize news ?

render_analyst_info(option)

###########
# INDICATORS #
###########
# TODO: Signals + more indicators
render_indicators(option, start_date, end_date)