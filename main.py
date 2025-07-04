from dhan_algo_trader.scheduler import run_scheduler
from dhan_algo_trader.websocket_handler import start_websocket

if __name__ == "__main__":
    start_websocket()
    run_scheduler()
