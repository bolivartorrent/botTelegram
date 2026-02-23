from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Tu token
TOKEN = '7852494996:AAGxQpNUj8ckm94GKBFYb0BjLnGOcpJQCjU'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Tu código aquí...
    pass

async def refer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Tu código aquí...
    pass

async def handle_start_param(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Tu código aquí...
    pass

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Tu código aquí...
    pass

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", handle_start))
    app.add_handler(CommandHandler("refer", refer))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("help", start))

    app.run_polling()

if __name__ == '__main__':
    main()
