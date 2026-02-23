import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv('7852494996:AAGxQpNUj8ckm94GKBFYb0BjLnGOcpJQCjU')

def start(update, context):
    update.message.reply_text('¡Hola! Soy tu bot de prueba.')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
print("El bot está en línea.")
