from telegram import Update, ReplyKeyboardRemove , ReplyKeyboardMarkup , KeyboardButton , WebAppInfo
from telegram.ext import CallbackContext

def remove_keyboard_ru(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Программа завершилась!😑",
        reply_markup=ReplyKeyboardRemove()
    )

def menu_handler_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
    chat_id=user.id,
    text = "Выберите одно из меню!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("🛍️ Разместить заказ!" , web_app=WebAppInfo('https://uzum.uz'))],
            [KeyboardButton("📦 Мои заказы!") , KeyboardButton("⚙️ Настройки!")],
            [KeyboardButton("ℹ️ О нас!") , KeyboardButton("✍️ Отправить комментарий!")],
            [KeyboardButton("🤕 Выйти из программы!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    
def settings_handler_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Изменить язык!⌨️",
        reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("English 🇺🇸") , KeyboardButton("Uzbek 🇺🇿")],
            [KeyboardButton("⬅️ Возвращаться!") , KeyboardButton("🤕 Выйти из программы!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))

def our_info_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Чтобы связаться с нами: https://muhammadrizomirzaev671@gmail.com !🪄"
    )
    
    bot.send_message(
    chat_id=user.id,
    text = "Ты делаешь что-нибудь еще??",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Возвращаться!") , KeyboardButton("🤕 Выйти из программы!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    
def send_idea_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Отправьте свое мнение: https://muhammadrizomirzaev671@gmail.com !🪄"
    )
    
    bot.send_message(
    chat_id=user.id,
    text = "Будете ли вы продолжать программу?!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Возвращаться!") , KeyboardButton("🤕 Выйти из программы!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))