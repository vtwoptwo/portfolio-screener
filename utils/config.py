import logging
import os
import ast
from dataclasses import dataclass
from dotenv import load_dotenv
import yahoo_fin.stock_info as si

load_dotenv()


# ['aapl', 'msft', 'goog', 'amzn', 'tsla']
# TODO: The configuration should be saved locally in a JSON in the static/config 
# folder (future implementation may allow for DB)
# TODO: Shares is directly related to the EITEN portfolio analysis library maybe some kind of "test your portfolio weights feature" could be implemented

# 📈 stock
# 🧺 basket
client_portfolio = {
    "aapl": {
        "name": "Apple",
        "logo": "https://logo.clearbit.com/apple.com",
        "price": si.get_live_price("aapl"),
        "shares": 10,
        "type": "📈" 
        
    }
    ,
    "msft": {
        "name": "Microsoft",
        "logo": "https://logo.clearbit.com/microsoft.com",
        "price": si.get_live_price("msft"),
        "shares": 10,
        "type": "📈"
    },
    "goog": {
        "name": "Google",
        "logo": "https://logo.clearbit.com/google.com",
        "price": si.get_live_price("goog"),
        "shares": 10,
        "type": "📈"
    },
    "amzn": {
        "name": "Amazon",
        "logo": "https://logo.clearbit.com/amazon.com",
        "price": si.get_live_price("amzn"),
        "shares": 10,
        "type": "📈" 


    },
    "tsla": {
        "name": "Tesla",
        "logo": "https://logo.clearbit.com/tesla.com",
        "price": si.get_live_price("tsla"),
        "shares": 10, 
        "type": "📈"

}, 
    "spy": {
        "name": "S&P 500",
        "logo": "https://logo.clearbit.com/spy.com",
        "price": si.get_live_price("spy"),
        "shares": 10,
        "type": "🧺" # basket


}
}


@dataclass
class Config:
    """
    Class for configuration of the environment
    """
    first_name: str
    last_name: str
    st_goal: int
    mt_goal: int
    lt_goal: int
    available_money: int
    client_portfolio: dict




 
# def config_local() -> Config:
#     """This function returns the configuration for the local environment"""
#     try:
#         return Config(openapi=os.getenv('OPENAI_API_KEY'),
#                     org=os.getenv('OPENAI_ORG'),
#                     type=os.getenv('OPENAI_API_TYPE'),
#                     version=os.getenv('OPENAI_API_VERSION'),
#                     controller=os.getenv('REDIS_CONTROLLER'),
#                     worker=os.getenv('REDIS_WORKER'), 
#                     endpoint=os.getenv('REDIS_ENDPOINT'),
#                     port=os.getenv('REDIS_PORT'),
#                     username=os.getenv('REDIS_USERNAME'))
    
#     except KeyError as ke:
#         raise ValueError(f'The env var {ke} is mandatory')


def config_from_env() -> Config:
    try: 
            return Config(first_name=os.getenv('FIRST_NAME'),
                        last_name=os.getenv('LAST_NAME'),
                        st_goal=os.getenv('ST_GOAL'),
                        mt_goal=os.getenv('MT_GOAL'),
                        lt_goal=os.getenv('LT_GOAL'),
                        available_money=os.getenv('AVAILABLE_MONEY'),
                        client_portfolio=client_portfolio)
    except KeyError as ke:
         raise ValueError(f'The env var {ke} is mandatory')


def create_logger(): 
    """This function creates a logger"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    if not os.path.exists('logs'):
        os.makedirs('logs')
    file_handler = logging.FileHandler('logs/assistente_privado.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger



# ------ CONSTANTS ------
LOG = create_logger()

config = config_from_env()
print(config)



