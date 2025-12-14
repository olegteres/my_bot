import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode
from telegram import InputFile


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
        "✔ Основы работы в 1С с нуля\n"
        "🤖 Навыки программирования через искусственный интеллект\n"
        "📂 Создание справочников, документов, отчетов\n"
        "📝 Запросы, регистры, формы, права\n"
        "🔗 Интеграции, обмены, API\n"
        "🏢 Реальные задачи бизнеса\n\n"

        "⏱ Длительность: 1–3 месяца в удобном темпе\n\n"

        "🎯 Итог: готовое резюме и навыки для работы на зарплату от 100 тыс./мес.\n\n"

        "📃 <a href=\"https://disk.yandex.ru/i/AXcGBPEQu97cbg\">Скачать программу</a>\n\n"
        
        "👉 Ознакомительный урок — /lesson\n"
        "🎁 То, что отличает этот курс — навык эффективного обучения, смотрите в подарках: /gift\n"
        "↪️ Главное меню — /start"
    )

    # отправляем текст
    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /lesson -----
async def lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎓 <b>Ознакомительный урок</b>\n\n"

        "Вот вводное занятие, которое покажет формат обучения и результат:\n"
        "📌 <a href=\"https://youtu.be/UCLuqQFZ-do\">Смотреть урок</a>\n\n"

        "После просмотра — посмотрите программу /program\n"
        "↪️ Вернуться в главное меню — /start"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


# ----- /prices -----
async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
    "💼 <b>Тарифы и цены</b>\n\n"

    "📗 <b>Самостоятельный</b> — 34 900 ₽\n"
    "✅ Доступ ко всем материалам курса\n"
    "📖 Учебные методички\n"
    "📝 Домашки без проверки\n"
    "💬 Чат студентов + поддержка куратора\n\n"
    
    "👉 Выбрать ""Самостоятельный"" — /howtopay\n\n"

    "🎯 <b>Наставник</b> — 54 900 ₽\n"
    "✅ Проверка всех домашних работ\n"
    "💡 Личные рекомендации по коду\n"
    "📞 1–2 мини-созвона в месяц\n"
    "💼 Помощь с портфолио и резюме\n"
    "🛠 Доп. примеры задач по 1С\n\n"

    "👉 Выбрать ""Наставник"" — /howtopay\n\n"

    "💎 <b>VIP (Профи)</b> — 74 900 ₽\n"
    "👨‍🏫 Личное менторство 1:1\n"
    "📋 Индивидуальный план и практика «под вакансию»\n"
    "🎯 Подготовка к собеседованиям\n"
    "📚 Подготовка к сертификации 1С\n"
    "💪 Максимальная поддержка до результата\n\n"

    "👉 Выбрать ""VIP (Профи)"" — /howtopay\n\n"

    "↪️ Главное меню — /start"
)

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /who -----
async def who(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "❓ <b>Подходит ли Вам?</b>\n\n"

        "👶 Никогда не работали в IT, но хотите попробовать\n"
        "💻 Знаете другой язык программирования и хотите стартовать в 1С\n"
        "🛠 Хотите стать разработчиком без математики и тяжёлого кода\n"
        "😴 Устали от скучной работы и хотите востребованную профессию\n"
        "🤖 Хотели бы использовать искусственный интеллект профессионально\n\n"

        "💡 Если 1–2 пункта совпадают — курс подходит.\n\n"

        "👉 Тарифы — /prices\n"
        "↪️ Главное меню — /start"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /howtopay -----
async def howtopay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🔥 <b>Как оплатить</b>\n\n"

        "Оплата принимается:\n"
        "💳 Карта (СБП / Visa / Mastercard) — просто отсканируйте QR-код ниже\n"
        "🫰 <a href=\"https://disk.yandex.ru/i/IrTlb3CTNBh3Zg\">Открыть QR-код</a>\n\n"

        "💼 Счёт на ИП или юр.лицо\n"
        "🌍 Зарубежные банки\n\n"

        "Если что-то не получается, напишите мне: 👉 <a href=\"https://t.me/olegtereschenko1\">в Telegram</a>\n"
        "↪️ Вернуться в главное меню — /start"
    )

     # Сначала отправляем текст
    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /gift -----
async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎁 <b>Подарочные материалы</b>\n\n"

        "🎯 Бонусный блок курса - Привычка учиться. Навык, который гарантирует достижение вашей цели:\n"
        "📃 <a href=\"https://disk.yandex.ru/i/9RA8UxzByO9pOA\">Скачать</a>\n\n"
        
        "↪️ Главное меню — /start"
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
