from telegram import Update, ReplyKeyboardMarkup, KeyboardButton , ReplyKeyboardRemove , WebAppInfo
from telegram.ext import CallbackContext
def contact(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text = "Iltimos , telefon raqamingizni yuboring!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [KeyboardButton("📞 Contact" , request_contact=True)]
            ],
            resize_keyboard=True,
            one_time_keyboard=True))
    
    
def contact_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot

    bot.send_message(
        chat_id=user.id,
        text="Telefon raqamingizni yuborganingiz uchun tashakkur😍🥰!"
    )

        
    bot.send_message(
    chat_id=user.id,
    text = "Menulardan birini tanlang!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("🛍️ Buyurtma berish" , web_app=WebAppInfo('https://uzum.uz'))],
            [KeyboardButton("📦 Buyurtmalarim!") , KeyboardButton("⚙️ Sozlamalar!")],
            [KeyboardButton("ℹ️ Biz haqimizda!") , KeyboardButton("✍️ Fikr qoldirish!")],
            [KeyboardButton("🤕 Dasturni tark etish!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))