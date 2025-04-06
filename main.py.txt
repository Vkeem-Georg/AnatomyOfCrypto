from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция, которая будет вызвана при команде /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш бот.')

def main():
    # Получаем токен из переменной окружения
    import os
    token = os.getenv('TELEGRAM_TOKEN')

    # Создаем объект Updater и передаем ему токен бота
    updater = Updater(token)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик для команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при завершении работы скрипта
    updater.idle()

if __name__ == '__main__':
    main()
