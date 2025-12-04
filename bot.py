import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "друг"

    text = (
        f"Добро пожаловать, {name} 😊🤝\n"
        "Этот бот поможет Вам за 2–3 минуты понять главное: подходит ли Вам курс, "
        "какие результаты Вы получите и какой тариф выбрать.\n\n"
        "Выберите раздел ниже:\n\n"
        "📘 Программа курса — /program\n"
        "🎓 Ознакомительный урок — /lesson\n"
        "💼 Тарифы и цены — /prices\n"
        "❓ Подходит ли мне? — /who\n"
        "🔥 Как оплатить — /howtopay\n"
        "🎁 Подарочные материалы — /gift\n\n"
        "Если нужно обратиться лично — <a href=\"https://t.me/olegtereschenko1\">напишите мне</a>."
    )

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def main():
    token = os.getenv("BOT_TOKEN")  # считываем переменную окружения
    if not token:
        raise ValueError("Переменная окружения BOT_TOKEN не найдена!")

    app = Application.builder().token(token).build()

    # Команда /start
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен! Напишите ему в Telegram.")

    app.run_polling()


if __name__ == "__main__":
    main()
