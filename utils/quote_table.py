import streamlit as st
from utils.yfinance_scraper import get_quote_table, get_stats, get_balance_sheet


def render_quote_table(option):
    """
    Render Quote Table in the FE

    Parameters
    ----------
    option : str 
        The ticker symbol of the stock to query

    """

    st.header("Company Performance")

    # get the blanance sheet
    balance_sheet = get_quote_table(option)
    # create a dataframe out of the dictionary and name it df_{key}

    columns = st.columns(2)
    for n, key in enumerate(balance_sheet):
        with columns[n%2]:
            st.button(f"**{key}**: {balance_sheet[key]}")
        