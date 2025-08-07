from telegram import Update, ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def my_order_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text = f"{user.first_name} ваш список заказов все еще пуст!😊"
    )
    bot.send_message(
        chat_id=user.id,
        text = "Мы ждем вашего заказа!😉"
    )
    
    bot.send_message(
    chat_id=user.id,
    text = "Ты можешь сделать это снова!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Возвращаться!") , KeyboardButton("🤕 Выйти из программы!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))