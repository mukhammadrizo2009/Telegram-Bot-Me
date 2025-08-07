from telegram import Update, ReplyKeyboardMarkup, KeyboardButton , ReplyKeyboardRemove , WebAppInfo
from telegram.ext import CallbackContext

def menu_handler(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
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
    
def my_order(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text = f"{user.first_name} buyurtmalar ro'yhatingiz hali bo'sh!😊"
    )
    bot.send_message(
        chat_id=user.id,
        text = "Buyurtma berishingizni kutub qolamiz!😉"
    )
    
    bot.send_message(
    chat_id=user.id,
    text = "Yana amal bajarishing mumkin!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Orqaga qaytish!") , KeyboardButton("🤕 Dasturni tark etish!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    

def remove_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Dastur tugatildi!😑 / The program has ended!😑 / Программа завершилась! 😑",
        reply_markup=ReplyKeyboardRemove()
    )
    
def settings_handler(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Tilni o'zgartirish!⌨️",
        reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("English 🇺🇸") , KeyboardButton("Русский 🇷🇺")],
            [KeyboardButton("⬅️ Orqaga qaytish!") , KeyboardButton("🤕 Dasturni tark etish!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    
    bot.send_message(
    chat_id=user.id,
    text = "Botda yana biror ishingiz bormi?",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Orqaga qaytish!") , KeyboardButton("🤕 Dasturni tark etish!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))

def our_info(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Bizga bog'lanish uchun: https://muhammadrizomirzaev671@gmail.com !🪄"
    )
    
    
    bot.send_message(
    chat_id=user.id,
    text = "Yana biror amal bajarasizmi?",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Orqaga qaytish!") , KeyboardButton("🤕 Dasturni tark etish!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    
def send_idea(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Fikringizni yuboring: https://muhammadrizomirzaev671@gmail.com !🪄"
    )
    
    
    bot.send_message(
    chat_id=user.id,
    text = "Dasturda davom etasizmi?!",
    reply_markup= ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("⬅️ Orqaga qaytish!") , KeyboardButton("🤕 Dasturni tark etish!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    ))
