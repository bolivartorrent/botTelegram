from telegram.ext import Updater, MessageHandler, Filters

# Reemplaza con el token de tu bot
TOKEN = '7852494996:AAGxQpNUj8ckm94GKBFYb0BjLnGOcpJQCjU'

def start(update, context):
    update.message.reply_text('¡Hola! Soy tu bot de Telegram.')

def echo(update, context):
    update.message.reply_text('Recibí tu mensaje: ' + update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Comando /start
    dp.add_handler(MessageHandler(Filters.command, start))
    # Responder a cualquier mensaje
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
