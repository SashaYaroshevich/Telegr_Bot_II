# Настройки
from urllib import response
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='5046886097:AAERgYymE0SZ1qm8bD-Uj0tCiJbB-rAN_m0')  # Токен API к Telegram
dispatcher = updater.dispatcher
from telegram import Update
from telegram.ext import CallbackContext
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, давай общаться!!!")


from telegram.ext import CommandHandler


def getMessageFromCLient(update: Update, context: CallbackContext):
    response = 'Получил ваше сообщение ' + update.message.text
    context.bot.send_message(chat_id=update.message.chat_id, text=response)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
text_message_handler = MessageHandler(Filters.text, getMessageFromCLient)
dispatcher.add_handler(text_message_handler)

updater.start_polling()