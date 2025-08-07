from telegram import Update, ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def my_order_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text = f"{user.first_name} your order list is still empty!😊"
    )
    bot.send_message(
        chat_id=user.id,
        text = "We are waiting for your order!😉"
    )
    
    bot.send_message(
    chat_id=user.id,
    text = "You can do it again!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Go back!") , KeyboardButton("🤕 Exit the program!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))