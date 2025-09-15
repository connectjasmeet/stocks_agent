import yfinance as yf
import json
import time
from datetime import datetime

# Load config
with open("config.json") as f:
    config = json.load(f)

stocks = config["stocks"]
buy_thresholds = config["buy_thresholds"]
sell_thresholds = config["sell_thresholds"]
interval = config["check_interval_seconds"]

def fetch_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1m")["Close"].iloc[-1]
    return round(price, 2)

def reason_and_act(ticker, price):
    # Reasoning
    if price <= buy_thresholds[ticker]:
        action = "BUY"
    elif price >= sell_thresholds[ticker]:
        action = "SELL"
    else:
        action = "HOLD"
    return action

def log_action(ticker, price, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] {ticker} Price: ${price} → Action: {action}"
    print(log_msg)
    with open("agent_log.txt", "a") as f:
        f.write(log_msg + "\n")

def run_agent():
    print("Starting ReAct-style Stock Agent...")
    while True:
        for ticker in stocks:
            try:
                price = fetch_price(ticker)
                action = reason_and_act(ticker, price)
                log_action(ticker, price, action)
            except Exception as e:
                print(f"Error fetching {ticker}: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    run_agent()
