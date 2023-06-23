import streamlit as st
import pandas as pd
import numpy as np
import yahoo_fin.stock_info as si
from utils.config import config, LOG


def render_analyst_info(option: str):
    """
    Render Analyst Info in the FE
    
    Parameters
    ----------
    option : str 
        The ticker symbol of the stock to query

    """

    st.header("Analysts Info")

    try: 
        data_analyst_info = si.get_analysts_info(option)   
    except:
        st.error("No Analyst Info available for this stock")
        return 404
    
    for key in data_analyst_info:
        # create a dataframe out of the dictionary
        df = pd.DataFrame(data_analyst_info[key])
        # print the name of the dataframe
        expander = st.expander(key)
        expander.write(df)
        
    return 200

