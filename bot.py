import os

from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode


# ----- /start -----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name or "друг"
    start_param = None
    if context.args:
        start_param = context.args[0]

    text = (
        f"Добро пожаловать, {name}.\n\n"
        
        "Меня зовут Олег, я коуч по 1С-программированию с десятилетним опытом😊🤝\n\n"

        "В начале 2025 попал под сокращение, за 3 месяца\n"
        "самостоятельно освоил 1С с нуля и нашел работу.\n\n"

        "Я на своем опыте понял, что не только знания и навыки влияют на старт карьеры.\n"
        "Не менее важно научиться подать себя на собеседовании и уметь использовать ИИ.\n"
        "Благодаря своему опыту в коучинге я умею вести человека с новичка — до зарплаты 100 тысяч в месяц.\n\n"
        
        "📌 За 3 месяца мои ученики:\n"
        "– осваивают 1С с нуля\n"
        "– понимают, что реально требуют работодатели\n"
        "– выходят на доход от 100 000 ₽\n\n"

        "Нажмите кнопку ниже — за 2–3 минуты покажу чёткий пошаговый путь входа в 1С 👇\n\n"

        "📘 Программа курса — /program\n"
        "🎓 Ознакомительный урок — /lesson\n"
        "💼 Тарифы и цены — /prices\n"
        "❓ Подходит ли мне? — /who\n"
        "🔥 Как оплатить — /howtopay\n"
        "🎁 Подарочные материалы — /gift\n\n"

        "Если нужно обратиться лично — "
        "<a href=\"https://t.me/olegtereschenko1\">напишите мне</a>."
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
        "🎁 Что отличает курс — /gift\n"
        "↪️ Главное меню — /start"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /lesson -----
async def lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎓 <b>Ознакомительный урок</b>\n\n"
        "Вот вводное занятие, которое покажет формат обучения и результат:\n\n"
        "📌 <a href=\"https://youtu.be/pZnkZkJq7tA\">YouTube</a>\n"
        "📌 <a href=\"https://rutube.ru/video/private/bcc308d10fc258557c41604dbbc0a387/?p=ZLHy3HNpOq73GjbTx-CWng\">RuTube</a>\n"
        "📌 <a href=\"https://disk.yandex.ru/i/to_b-4Nr3EswJg\">Яндекс.Диск</a>\n\n"
        "После просмотра — /program\n"
        "↪️ Главное меню — /start"
    )

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


# ----- /prices -----
async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💼 <b>Тарифы и цены</b>\n\n"
        "📗 <b>Самостоятельный</b> — 34 900 ₽\n"
        "✅ Материалы курса\n"
        "📖 Методички\n"
        "📝 Домашки без проверки\n"
        "💬 Чат + куратор\n\n"
        "👉 Выбрать — /howtopay\n\n"
        "🎯 <b>Наставник</b> — 54 900 ₽\n"
        "✅ Проверка ДЗ\n"
        "💡 Рекомендации по коду\n"
        "📞 Созвоны\n"
        "💼 Портфолио и резюме\n\n"
        "👉 Выбрать — /howtopay\n\n"
        "💎 <b>VIP</b> — 74 900 ₽\n"
        "👨‍🏫 Менторство 1:1\n"
        "🎯 Под вакансии\n"
        "📚 Сертификация\n\n"
        "👉 Выбрать — /howtopay\n\n"
        "↪️ Главное меню — /start"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /who -----
async def who(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "❓ <b>Кому подходит мой курс?</b>\n\n"
        "👶 Новичкам в IT.\n"
        "💻 Программистам из других языков.\n"
        "🛠 Тем, кто хочет освоить программирование без сложной математики.\n"
        "😴 Тем, кто хочет сменить работу.\n"
        "🤖 Тем, кто хочет эффективно использовать ИИ.\n\n"
        "Если откликается — курс подходит.\n\n"
        "👉 /prices\n"
        "↪️ /start"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /howtopay -----
async def howtopay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🔥 <b>Как оплатить</b>\n\n"
        "💳 Карта / СБП\n"
        "🫰 <a href=\"https://disk.yandex.ru/i/IrTlb3CTNBh3Zg\">QR-код</a>\n\n"
        "💼 Счёт / зарубежные банки — "
        "<a href=\"https://t.me/olegtereschenko1\">написать</a>\n\n"
        "↪️ /start"
    )

    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


# ----- /gift -----
async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎁 <b>Подарочные материалы</b>\n\n"
        "🎯 Привычка учиться:\n"
        "<a href=\"https://disk.yandex.ru/i/9RA8UxzByO9pOA\">Скачать</a>\n\n"
        "😶‍🌫️ VPN инструкция:\n"
        "<a href=\"https://disk.yandex.ru/i/sBwF93ineoTdyg\">Скачать</a>\n\n"
        "🤖 ИИ для работы:\n"
        "<a href=\"https://disk.yandex.ru/i/Ca5GHgSGjVK8Cw\">Скачать</a>\n\n"
        "↪️ /start"
    )

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN не найден")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("program", program))
    app.add_handler(CommandHandler("lesson", lesson))
    app.add_handler(CommandHandler("prices", prices))
    app.add_handler(CommandHandler("who", who))
    app.add_handler(CommandHandler("howtopay", howtopay))
    app.add_handler(CommandHandler("gift", gift))

    print("Бот запущен")
    app.run_polling()


if __name__ == "__main__":
    main()
