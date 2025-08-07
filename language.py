from telegram import Update, ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def language(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id , 
        text = "Iltimos dastur tilini tanlang! 🇺🇿\
Please select the program language! 🇺🇸\
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
    