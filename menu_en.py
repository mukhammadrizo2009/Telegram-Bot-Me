from telegram import Update, ReplyKeyboardRemove , ReplyKeyboardMarkup , KeyboardButton , WebAppInfo
from telegram.ext import CallbackContext

def remove_keyboard_en(update: Update, context: CallbackContext):
    update.message.reply_text(
        "The program has ended!😑",
        reply_markup=ReplyKeyboardRemove()
    )

def menu_handler_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
    chat_id=user.id,
    text = "Choose one of the menus!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("🛍️ Place an order!" , web_app=WebAppInfo('https://uzum.uz'))],
            [KeyboardButton("📦 My orders!") , KeyboardButton("⚙️ Settings!")],
            [KeyboardButton("ℹ️ about Us!") , KeyboardButton("✍️ Send a comment!")],
            [KeyboardButton("🤕 Exit the program!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    
def settings_handler_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Change language!⌨️",
        reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("Русский 🇷🇺") , KeyboardButton("Uzbek 🇺🇿")],
            [KeyboardButton("⬅️ Go back!") , KeyboardButton("🤕 Exit the program!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))

def our_info_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "To contact us: https://muhammadrizomirzaev671@gmail.com !🪄"
    )
    
    bot.send_message(
    chat_id=user.id,
    text = "Do you do anything else?",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Go back!") , KeyboardButton("🤕 Exit the program!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    
def send_idea_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Submit your opinion: https://muhammadrizomirzaev671@gmail.com !🪄"
    )
    
    bot.send_message(
    chat_id=user.id,
    text = "Will you continue with the program?!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Go back!") , KeyboardButton("🤕 Exit the program!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))