kline = dict(tickers = ['BTCUSDT', 'ETHBTC'],          # List of tickers. Leave empty to request all the updated tickers on binance.
             intervals = ['5min''15min''30min''1h'],    # List with multiple intervals if desired: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
             n_periods = 200,       # Number of periods to analise
             start_time = '',       # Start of the period to analise: '14 Sep, 2018'
             end_time = '')         # End of the period to analise: '29 Sep, 2018'

live_bot = dict(live = True,                   # Make the bot run on an infinite loop and perform the analysis every `sleep` seconds.
                sleep = 20,                     # Sleep time for the live bot to not overload the Binance API.
                threading = True,               # Multithreading boolean. Makes the Bot faster when set to True.
                telegram_token = '852816659:AAFIXmwcd3s0KqXWjQ42A6g9OTC367X_xTs',            # Telegram token of the Bot created with BotFather
                telegram_chat_id = ['469284226'],        # Telegram channel id
                discord_web_hook = ['https://discord.com/api/webhooks/1002286132043714640/kYjKJcmP5IHCJCpCYOtHIetNSFUM4eSmiJGhHLjf7OpVpjuLwrEwjVn5qpt-lOWRfLAj'])        # Discord server webhook
