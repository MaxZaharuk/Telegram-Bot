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