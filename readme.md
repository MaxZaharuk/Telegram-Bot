This is a telegram bot which can get forex and crypto charts and some technical indicators.

Used technology:
* Python 3.11.2;
* aiogram 3.0.0b6;
* aiosqlite (database);
* Redis (persistent storage for some ongoing data);
* matplotlib 3.6.3
* pandas 1.5.3
* aiohttp 3.8.3

Before you run:
1. Rename file "env_template" to ".env"
2. Inside .env change constants values to yours
3. Run main.py

P.S. Additionally to install all packages from "requirements.txt" do not forget to execute in terminal: "pip install mpl_finance"


Basic functional:

* commands "/start" and "/help" to start bot or get help to start
* language choice (it could be changed anytime)
* queries history to see last 5 queries
* market choice: forex or crypto
* instrument choice like e.g. EURUSD or BTCUSD
* timeseries choice: daily, weekly, monthly
* after all bot will send some plots: one with chosen instrument on chosen timeseries and three with technical indicators (SMA, EMA, MACD)
* subscribe service is still in development