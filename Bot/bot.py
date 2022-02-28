# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from urllib import response
import apiai, json

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
request = apiai.ApiAI('ВАШ API ТОКЕН').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'BatlabAIBot' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update.message.text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        context.bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
       context.bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
text_message_handler = MessageHandler(Filters.text, getMessageFromCLient)
dispatcher.add_handler(text_message_handler)

updater.start_polling()