import telebot

bot = telebot.TeleBot("5046886097:AAERgYymE0SZ1qm8bD-Uj0tCiJbB-rAN_m0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)

bot.infinity_polling()