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


###########
# INDICATORS #
###########
# Download data


def render_indicators(option:str, start_date:str, end_date):

    """
    Render Indicators in the FE


    Parameters
    ----------
    option : str 
        The ticker symbol of the stock to query
    start_date : datetime.date

    end_date : datetime.date

    """

    try: 
        df = si.get_data(option, start_date, end_date)
    except:
        st.error("No Data available for this stock")
        return 404

    # Bollinger Bands
    indicator_bb = BollingerBands(df['close'])
    bb = df
    bb['bb_h'] = indicator_bb.bollinger_hband()
    bb['bb_l'] = indicator_bb.bollinger_lband()
    bb = bb[['close','bb_h','bb_l']]

    # Moving Average Convergence Divergence
    macd = MACD(df['close']).macd()

    # Resistence Strength Indicator
    rsi = RSIIndicator(df['close']).rsi()
    stochastic_rsi = StochRSIIndicator(df['close']).stochrsi()

    # Plot the prices and the bolinger bands
    st.header("Indicators")
    expander_bb = st.expander("Bollinger Bands")
    expander_bb.line_chart(bb)

    expander_macd = st.expander("Moving Average Convergence Divergence")
    expander_macd.line_chart(macd)

    expander_rsi = st.expander("Resistence Strength Indicator")
    # create two lines in the same chart
    expander_rsi.line_chart(rsi)
    expander_rsi.line_chart(stochastic_rsi)
    return 200

