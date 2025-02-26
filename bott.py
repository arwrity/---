import logging
import wikipediaapi
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Установка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Ссылка на ресурс
WIKI_API_URL = "https://ru.wiktionary.org/w/api.php"

# Создание экземпляра Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('ru')


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Введите слово, чтобы получить его описание из Википедии.')


def get_description(word: str) -> str:
    page = wiki_wiki.page(word)
    if page.exists():
        return page.summary
    else:
        return 'Извините, я не нашел информацию по этому слову.'


def handle_message(update: Update, context: CallbackContext) -> None:
    word = update.message.text
    description = get_description(word)
    update.message.reply_text(description)


def main() -> None:
    # Вставьте ваш токен здесь
    updater = Updater("7748208277:AAFFDjr_-sZ4Q2JtNb9IXv-Ab3kTL1MbjRc")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    logging.info("Бот запущен. Нажмите Ctrl+C для остановки.")
    updater.idle()


if __name__ == '__main__':
    main()