import streamlit as st
import pandas as pd
from yahoo_fin.news import get_yf_rss


def render_news(option: str):
    """
    Render News in the FE
    
    Parameters
    ----------
    option : str 
        The ticker symbol of the stock to query

    """
    st.header("News")

    news = get_yf_rss(option)
    columns = st.columns(2)
    for i in range(4):
        with columns[i%2]:
            expander_news = st.expander(news[i].title)
            expander_news.write(f"{news[i].summary} [Read More...]({news[0].summary_detail.base})")



