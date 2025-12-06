import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode


# ----- /start -----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name or "друг"

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


# ----- /program -----
async def program(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📘 <b>Программа курса</b>\n\n"
        "Вы изучите:\n"
        "✔ основы работы в 1С\n"
        "✔ создание справочников, документов, отчетов\n"
        "✔ запросы, регистры, формы, права\n"
        "✔ интеграции, обмены, API\n"
        "✔ реальные задачи бизнеса\n\n"
        "⏱ Длительность: 1–3 месяца в удобном темпе\n\n"
        "🎯 Итог: готовое портфолио и навыки для работы.\n\n"
        "👉 Посмотрите ознакомительный урок — /lesson"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /lesson -----
async def lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎓 <b>Ознакомительный урок</b>\n\n"
        "Вот вводное занятие, которое покажет формат обучения и результат:\n"
        "📌 <a href=\"https://youtu.be/UCLuqQFZ-do\">Смотреть урок</a>\n\n"
        "После просмотра — посмотрите программу /program"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


# ----- /prices -----
async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
    "💼 <b>Тарифы и цены</b>\n\n"
    "🔥 <b>Самостоятельный</b> — 34 900 ₽\n"
    "📌 Доступ ко всем материалам курса\n"
    "📌 Учебные методички\n"
    "📌 Домашки без проверки\n"
    "📌 Чат студентов + поддержка куратора\n\n"

    "🔥 <b>Наставник</b> — 54 900 ₽\n"
    "📌 Проверка всех домашних работ\n"
    "📌 Личные рекомендации по коду\n"
    "📌 1–2 мини-созвона в месяц\n"
    "📌 Помощь с портфолио и резюме\n"
    "📌 Доп. примеры задач по 1С\n\n"

    "🔥 <b>VIP (Профи)</b> — 74 900 ₽\n"
    "📌 Личное менторство 1:1\n"
    "📌 Индивидуальный план и практика «под вакансию»\n"
    "📌 Подготовка к собеседованиям\n"
    "📌 Подготовка к сертификации 1С\n"
    "📌 Максимальная поддержка до результата\n\n"

    "👉 Как оплатить — /howtopay"
)

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /who -----
async def who(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "❓ <b>Подходит ли Вам?</b>\n\n"
        "✔ Никогда не работали в 1С, но хотите попробовать\n"
        "✔ Вы программист и хотите получать больше\n"
        "✔ Хотите перейти в IT без математики и тяжёлого кода\n"
        "✔ Устали от скучной работы и хотите востребованную профессию\n\n"
        "💡 Если 1–2 пункта совпадают — курс подходит.\n\n"
        "👉 Смотрите тарифы — /prices"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /howtopay -----
async def howtopay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🔥 <b>Как оплатить</b>\n\n"
        "Оплата принимается:\n"
        "💳 Карта (СБП / Visa / Mastercard)\n"
        "💼 Счёт на ИП или юр.лицо\n"
        "🌍 Зарубежные банки (по запросу)\n\n"
        "Напишите мне и я пришлю инструкцию: 👉 <a href=\"https://t.me/olegtereschenko1\">в Telegram</a>"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /gift -----
async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎁 <b>Подарочные материалы</b>\n\n"
        "Дарю: чек-лист «Как не слиться в 1С и быстро выйти на доход»:\n"
        "📌 <a href=\"https://docs.google.com/document/d/1PBDUuAvIWb_IM9oBn7EnAbbC98tFq-6i_xA9k4f9PlM\">Скачать</a>\n\n"
        "Плюс бонус: <b>шаблон резюме 1С-программиста</b> — отправлю лично 👉 <a href=\"https://t.me/olegtereschenko1\">запросить</a>"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


# ------ Main ------
def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Переменная окружения BOT_TOKEN не найдена!")

    app = Application.builder().token(token).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("program", program))
    app.add_handler(CommandHandler("lesson", lesson))
    app.add_handler(CommandHandler("prices", prices))
    app.add_handler(CommandHandler("who", who))
    app.add_handler(CommandHandler("howtopay", howtopay))
    app.add_handler(CommandHandler("gift", gift))

    print("Бот запущен! Напишите ему в Telegram.")
    app.run_polling()


if __name__ == "__main__":
    main()
