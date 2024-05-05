import requests
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6998088334:AAEaD7WVYbfpk8L85udfl5qm0TSdPMPTaqI'
CRYPTO_NAME_TO_TICKER = {
    "Bitcoin": "BTCUSDT",
    "Ethereum": "ETHUSDT",
}

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(row_width=2)
    for crypro_name in CRYPTO_NAME_TO_TICKER.keys():
        item_button = KeyboardButton(crypro_name)
        markup.add(item_button)
    bot.send_message(message.chat.id, "Choose a crypto", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in CRYPTO_NAME_TO_TICKER.keys())
def send_price(message):
    crypto_name = message.text
    ticker = CRYPTO_NAME_TO_TICKER[crypto_name]
    price = get_price_by_ticker(ticker=ticker)
    bot.send_message(message.chat.id, f'Price of {crypto_name} to USDT is {price}')


def get_rice_by_ticker(*, ticker):
    endpoint = "https://api.binance.com/api/v3/ticker/price"
    params = {
        'symbol': ticker,
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    price = round(float(data["price"]), 2)
    return price


bot.infinity_polling()
