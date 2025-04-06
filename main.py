from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот AnatomyOfCrypto. Готов принимать сигналы.")

def main():
    token = os.getenv("BOT_TOKEN")  # Убедись, что переменная в Render называется именно BOT_TOKEN

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
