import os

from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram.constants import ParseMode


def menu_buttons(commands: list[str]):

    buttons_map = {
        "contact": ("💬 Написать лично", "https://t.me/olegtereschenko1"),
        "program": ("📘 Программа курса", "program"),
        "lesson": ("🎓 Ознакомительный урок", "lesson"),
        "prices": ("💼 Тарифы и цены", "prices"),
        "who": ("❓ Подходит ли мне", "who"),
        "howtopay": ("🔥 Как оплатить", "howtopay"),
        "gift": ("🎁 Подарки", "gift"),
        "start": ("↪️ Главное меню", "start"),
        
        "buy_basic": ("📗 Выбрать Самостоятельный — 34 900 ₽", "buy_basic"),
        "buy_mentor": ("🎯 Выбрать Наставник — 54 900 ₽ ⭐", "buy_mentor"),
        "buy_vip": ("💎 Выбрать VIP — 74 900 ₽", "buy_vip"),
    }

    keyboard = []

    for cmd in commands:
        text, action = buttons_map[cmd]

        if action.startswith("http"):
            button = InlineKeyboardButton(text=text, url=action)
        else:
            button = InlineKeyboardButton(text=text, callback_data=action)

        keyboard.append([button])

    return InlineKeyboardMarkup(keyboard)


async def send_or_edit(update, text, reply_markup=None, preview=True):

    if update.callback_query:
        query = update.callback_query

        try:
            await query.edit_message_text(
                text=text,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=not preview,
                reply_markup=reply_markup
            )
        except Exception:
            pass

    elif update.message:
        await update.message.reply_text(
            text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=not preview,
            reply_markup=reply_markup
        )
        


# ----- /start -----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    name = update.effective_user.first_name or "друг"

    text = (
        f"Добро пожаловать, {name}.\n\n"
        
        "Меня зовут Олег, я коуч по 1С-программированию с десятилетним опытом😊🤝\n\n"

        "В начале 2025 попал под сокращение, за 3 месяца самостоятельно освоил 1С с нуля и нашел работу.\n\n"

        "Я на своем опыте понял, что не только знания и навыки влияют на старт карьеры. Не менее важно научиться подать себя на собеседовании и уметь использовать ИИ. Благодаря своему опыту в коучинге я умею вести человека с новичка — до зарплаты 100 тысяч в месяц.\n\n"
        
        "📌 За 3 месяца мои ученики:\n"
        "– осваивают 1С с нуля\n"
        "– понимают, что реально требуют работодатели\n"
        "– выходят на доход от 100 000 ₽\n\n"

        "Нажмите кнопку ниже — за 2–3 минуты покажу чёткий пошаговый путь входа в 1С 👇\n\n"
    )

    await send_or_edit(
        update,
        text,
        menu_buttons(["contact", "program", "lesson", "prices", "who", "howtopay", "gift"])
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
    )

    await send_or_edit(
        update,
        text,
        menu_buttons(["lesson","gift","start"])
    )


# ----- /lesson -----
async def lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = (
        "🎓 <b>Ознакомительный урок</b>\n\n"

        "Вот вводное занятие, которое покажет формат обучения и результат:\n\n"
        
        "📌 <a href=\"https://youtu.be/pZnkZkJq7tA\">YouTube</a>\n"
        "📌 <a href=\"https://rutube.ru/video/private/bcc308d10fc258557c41604dbbc0a387/?p=ZLHy3HNpOq73GjbTx-CWng\">RuTube</a>\n"
        "📌 <a href=\"https://disk.yandex.ru/i/to_b-4Nr3EswJg\">Яндекс.Диск</a>\n\n"
    )

    await send_or_edit(
    update,
    text,
    menu_buttons(["program","start"])
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

        # "👉 Выбрать — /howtopay\n\n"
        "🎯 <b>Наставник</b> — 54 900 ₽\n"
        "➕ Всё, что в Самостоятельном\n"
        "💡 Рекомендации по коду\n"
        "📞 Личные созвоны\n"
        "💼 Подготовка портфолио и резюме\n\n"

        # "👉 Выбрать — /howtopay\n\n"
        "💎 <b>VIP</b> — 74 900 ₽\n"
        "➕ Всё, что в Наставнике\n"
        "👨‍🏫 Менторство 1:1\n"
        "🎯 Подготовка под вакансии\n"
        "📚 Помощь с сертификацией 1С\n\n"

        # "👉 Выбрать — /howtopay\n\n"
        # "↪️ Главное меню — /start"
    )

    await send_or_edit(
    update,
    text,
    menu_buttons([
        "buy_basic",
        "buy_mentor",
        "buy_vip",
        "start"
    ])
)


# ----- /who -----
async def who(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = (
        "❓ <b>Кому подходит мой курс?</b>\n\n"

        "👶 Новичкам в сфере айти.\n"
        "💻 Программистам из других языков.\n"
        "😴 Тем, кто хочет сменить работу.\n"
        "🛠 Освоить программирование без сложной математики.\n"
        "🤑 Тем, кто хочет зарабатывать намного больше, чем сейчас.\n"
        "🤖 Желающим эффективно использовать ИИ.\n\n"

        "Если откликается — курс подходит.\n\n"
    )

    await send_or_edit(
    update,
    text,
    menu_buttons(["prices", "start"])
)


# ----- /howtopay -----
async def howtopay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = (
        "🔥 <b>Как оплатить</b>\n\n"
        
        "✅ Если вы выбрали тариф курса, оплатите <b>стоимость выбранного тарифа</b> любым способом ниже.\n\n"

        "💳 Карта / СБП\n"
        "🫰 <a href=\"https://disk.yandex.ru/i/IrTlb3CTNBh3Zg\">QR-код</a>\n\n"

        "💼 Счёт / зарубежные банки — "
        "<a href=\"https://t.me/olegtereschenko1\">написать</a>\n\n"
        
        "⚠️ После оплаты отправьте чек в личные сообщения."
    )

    await send_or_edit(
    update,
    text,
    menu_buttons(["contact", "prices", "start"])
    )


# ----- /gift -----
async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = (
        "🎁 <b>Подарочные материалы</b>\n\n"

        "🎯 Привычка учиться (навык гарантированного достижения цели):\n"
        "<a href=\"https://disk.yandex.ru/i/9RA8UxzByO9pOA\">Скачать</a>\n\n"

        "😶‍🌫️ VPN инструкция:\n"
        "<a href=\"https://disk.yandex.ru/i/A2RxHrPoiy9C-A\">Скачать</a>\n\n"

        "🤖 ИИ для работы:\n"
        "<a href=\"https://disk.yandex.ru/i/Ca5GHgSGjVK8Cw\">Скачать</a>\n\n"
    )

    await send_or_edit(
    update,
    text,
    menu_buttons(["start"])
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    await query.answer()

    handlers = {
    "start": start,
    "program": program,
    "lesson": lesson,
    "prices": prices,
    "who": who,
    "howtopay": howtopay,
    "gift": gift,

    "buy_basic": howtopay,
    "buy_mentor": howtopay,
    "buy_vip": howtopay,
    }

    handler = handlers.get(query.data)
    if handler:
        await handler(update, context)


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

    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущен")
    app.run_polling()


if __name__ == "__main__":
    main()
