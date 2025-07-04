# DHAN_ALGO_TRADER Framework

The **DHAN_ALGO_TRADER** framework is a modular Python-based trading system designed to automate trading strategies. Below is an explanation of its structure and functionality:

---

## 1. Core Components

### `main.py`
- Acts as the entry point of the application.
- Initializes the WebSocket connection (via `start_websocket`) and starts the scheduler (via `run_scheduler`).

### `config.py`
- Stores configuration constants such as API keys, access tokens, and Telegram credentials.
- Used across the framework for authentication and notifications.

---

## 2. Trading Logic

### `strategy.py`
- Contains the trading strategy logic.
- The function `check_trade_signal` evaluates market data (e.g., LTP) and generates trade signals (e.g., BUY/SELL actions).

### `order_manager.py`
- Handles order placement.
- The function `place_bracket_order` is responsible for executing trades, including stop-loss (SL) and take-profit (TP) logic.

---

## 3. Data Handling

### `data_fetcher.py`
- Fetches live market data, such as the Last Traded Price (LTP), for a given symbol.
- This data is used by the strategy module.

### `websocket_handler.py`
- Manages WebSocket connections to receive real-time market updates.
- Currently, it contains a placeholder implementation.

---

## 4. Automation

### `scheduler.py`
- Automates the execution of the trading strategy at regular intervals using the `apscheduler` library.
- The function `run_scheduler` schedules the `run_strategy` function to execute every 5 minutes.

---

## 5. Notifications

### `alerts.py`
- Sends alerts via Telegram using the Telegram Bot API.
- The function `send_telegram_alert` is used to notify users about trade actions or other events.

---

## 6. Logging

### `logger.py`
- Logs trade-related information to a file (`trade.log`) for record-keeping and debugging purposes.
- The function `log_trade` writes trade details to the log.

---

## 7. Utilities

### `utils/`
- A placeholder directory for helper functions or reusable utilities.
- Currently, it contains empty files (`__init__.py` and `helpers.py`).

---

## Workflow

1. **Initialization**:
   - The application starts with `main.py`, which initializes the WebSocket and scheduler.

2. **Data Fetching**:
   - Market data is fetched using `fetch_ltp`.

3. **Signal Generation**:
   - The strategy module evaluates the data and generates trade signals.

4. **Order Placement**:
   - Orders are placed using the `place_bracket_order` function.

5. **Notifications and Logging**:
   - Alerts are sent via Telegram, and trade details are logged.

6. **Automation**:
   - The scheduler ensures the strategy runs periodically without manual intervention.