from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '7852494996:AAGxQpNUj8ckm94GKBFYb0BjLnGOcpJQCjU'

# Función para iniciar y explicar
def start(update, context):
    update.message.reply_text("¡Hola! Usa /refer para obtener tu enlace de referencia.")

# Función para generar el enlace de referencia
def refer(update, context):
    user_id = update.message.from_user.id
    referral_link = f"https://t.me/tu_bot_username?start={user_id}"
    update.message.reply_text(f"Comparte este enlace para invitar amigos: {referral_link}")

# Función para manejar el comando /start con parámetro
def handle_start(update, context):
    args = context.args
    if args:
        ref_id = args[0]
        # Aquí puedes guardar la referencia en tu base de datos
        update.message.reply_text(f"Has sido referido por usuario {ref_id}. ¡Gracias!")
    else:
        update.message.reply_text("¡Bienvenido!")

# Función para mostrar estadísticas (opcional)
def stats(update, context):
    # Aquí puedes mostrar tus estadísticas
    update.message.reply_text("Aquí tus estadísticas de referidos...")

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", handle_start))
    dp.add_handler(CommandHandler("refer", refer))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(CommandHandler("help", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
