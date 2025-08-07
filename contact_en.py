from telegram import Update, ReplyKeyboardMarkup, KeyboardButton , ReplyKeyboardRemove , WebAppInfo
from telegram.ext import CallbackContext
def contact_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text = "Please send your phone number!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [KeyboardButton("📞 Contact" , request_contact=True)]
            ],
            resize_keyboard=True,
            one_time_keyboard=True))
    
def contact_handler_en(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot

    bot.send_message(
        chat_id=user.id,
        text="Thank you for sending your phone number!😍🥰!"
    )

        
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