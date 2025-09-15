# stocks_agent
ReAct-style stock agent that tracks multiple stocks, reasons about them, and logs actions. This version is safe for testing (no real trades yet).

# ReAct Stock Agent

A simple ReAct-style agent that monitors stock prices and logs buy/sell/hold actions.

## Features
- Tracks multiple stocks
- Uses a reasoning loop (ReAct pattern)
- Logs actions to `agent_log.txt`
- Configurable thresholds and check interval

## Setup
```bash
git clone <repo_url>
cd react_stock_agent
pip install -r requirements.txt
python agent.py

