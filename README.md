# Telegram Bot Python

A telegram bot coded in Python which fetches the current stock price of the ticker requested.

## Setup

The following commands can be run to install the necessary packages to run the Python script:

Telegram Bot API
```bash
pip install pyTelegramBotAPI
```

Used to configure API_KEY from .env file for the Bot API to use as credentials.
```bash
pip install python-decouple
```

Used to access market data.
```bash
pip install yfinance
```

## Usage

The file "main.py" has the Python code and can be executed using below command in the terminal.

```bash
python main.py
```
Once the program is running, Telegram Bot is functional.

## Demonstration

### Telegram chat with Bot
![telegram chat](assets/screenshot0.png)

### Output in terminal while running
![terminal screen](assets/output.png)