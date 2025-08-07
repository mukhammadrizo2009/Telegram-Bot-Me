from telegram import Update, ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def start(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text = f"Assalomu alaykum {user.first_name}")
    
    bot.send_message(
        chat_id = user.id , 
        text = "Iltimos dastur tilini tanlang! 🇺🇿 \n\
Please select the program language! 🇺🇸 \n\
Пожалуйста, выберите язык программы! 🇷🇺",
            reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [KeyboardButton("Uzbek 🇺🇿")],
                [KeyboardButton("English 🇺🇸")],
                [KeyboardButton("Русский 🇷🇺")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True)
    )