from telegram import Update, ReplyKeyboardMarkup, KeyboardButton , ReplyKeyboardRemove , WebAppInfo
from telegram.ext import CallbackContext
def contact_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text = "Пожалуйста, пришлите свой номер телефона!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [KeyboardButton("📞 Contact" , request_contact=True)]
            ],
            resize_keyboard=True,
            one_time_keyboard=True))
    
def contact_handler_ru(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot

    bot.send_message(
        chat_id=user.id,
        text="Спасибо, что отправили свой номер телефона!😍🥰!"
    )

        
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