from telegram.ext import Updater, CommandHandler

# Reemplaza 'TU_TOKEN' con el token que te dio BotFather
TOKEN = '7852494996:AAGxQpNUj8ckm94GKBFYb0BjLnGOcpJQCjU'

def start(update, context):
    update.message.reply_text('¡Hola! Soy tu bot de Telegram.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
