from apscheduler.schedulers.blocking import BlockingScheduler
from dhan_algo_trader.strategy import check_trade_signal
from dhan_algo_trader.data_fetcher import fetch_ltp
from dhan_algo_trader.order_manager import place_bracket_order
from dhan_algo_trader.logger import log_trade

def run_strategy():
    data = fetch_ltp("RELIANCE")
    signal = check_trade_signal(data)
    if signal:
        place_bracket_order(signal)
        log_trade(signal)

def run_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(run_strategy, 'interval', minutes=5)
    scheduler.start()
