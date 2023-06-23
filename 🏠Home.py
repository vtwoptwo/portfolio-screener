import streamlit as st
import yahoo_fin.stock_info as si
from utils.config import config, LOG
# first there is going to be a configuration of your stock portfolio 
# It will include NAME, LASTNAME, short term goal, medium term goal, long term goal, how much money you currently have disposable to invest

# we can use jsons to render data of each config file

LOG.info(config)

st.title("Welcome " + config.first_name +",")
st.write("This is a simple web app to help you keep track of your stock portfolio")


n = len(config.client_portfolio)
st.write("You currently have " + str(n) + " stocks in your portfolio")


columns = st.columns(3)
for i, key in enumerate(config.client_portfolio):
    with columns[i%3]:
        st.header(config.client_portfolio[key]["name"])
        st.image(config.client_portfolio[key]["logo"], width=50)
        st.button("Price: " + str(round(config.client_portfolio[key]["price"], 2)))
        #expander
        expander = st.expander("More info")
        expander.write("Shares: " + str(config.client_portfolio[key]["shares"]))

        

