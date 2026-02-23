import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import json
import os

# Configuración del logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Archivo para guardar datos
DATA_FILE = 'referrals.json'

# Tu token del bot
TOKEN = '7852494996:AAGxQpNUj8ckm94GKBFYb0BjLnGOcpJQCjU'

# Cargar datos existentes o crear un nuevo diccionario
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
else:
    data = {}

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def start(update: Update, context: CallbackContext):
    user_id = str(update.message.from_user.id)
    if user_id not in data:
        data[user_id] = {'referrals': 0, 'referrer': None}
        save_data()
    update.message.reply_text(f"¡Hola {update.message.from_user.first_name}! Usa /refer para obtener tu enlace de referido.")

def refer(update: Update, context: CallbackContext):
    user_id = str(update.message.from_user.id)
    if user_id not in data:
        data[user_id] = {'referrals': 0, 'referrer': None}
    # El enlace de referido puede ser el ID del usuario
    referral_link = f"https://t.me/bolivartorrentbot?start={user_id}"
    update.message.reply_text(f"Comparte este enlace para referir a otros:\n{referral_link}")

def handle_start_param(update: Update, context: CallbackContext):
    args = context.args
    referrer_id = args[0] if args else None
    user_id = str(update.message.from_user.id)

    # Registrar referencia
    if referrer_id and referrer_id != user_id:
        if user_id not in data:
            data[user_id] = {'referrals': 0, 'referrer': referrer_id}
        if data[user_id]['referrer'] is None:
            data[user_id]['referrer'] = referrer_id
            # Incrementar referencias del referido
            if referrer_id in data:
                data[referrer_id]['referrals'] += 1
            else:
                data[referrer_id] = {'referrals':1, 'referrer': None}
            save_data()
            update.message.reply_text("¡Gracias por registrarte por referencia!")
        else:
            update.message.reply_text("Ya tienes un referidor registrado.")
    else:
        update.message.reply_text("Bienvenido!")

def stats(update: Update, context: CallbackContext):
    user_id = str(update.message.from_user.id)
    if user_id in data:
        referrals = data[user_id]['referrals']
        update.message.reply_text(f"Tienes {referrals} referidos.")
    else:
        update.message.reply_text("No tienes referidos todavía.")

def main():
    updater = Updater(7852494996:AAGxQpNUj8ckm94GKBFYb0BjLnGOcpJQCjU, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", handle_start_param))
    dp.add_handler(CommandHandler("refer", refer))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(CommandHandler("help", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
