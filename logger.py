import logging

logging.basicConfig(filename="trade.log", level=logging.INFO)

def log_trade(info):
    logging.info(info)
