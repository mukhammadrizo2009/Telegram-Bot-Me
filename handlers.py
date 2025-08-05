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
        text = f"Buyurtma berishingizni kutub qolamiz!😉"
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

def start(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text = f"Assalomu alaykum {user.first_name}")
    
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

def remove_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Dastur tugatildi!😑",
        reply_markup=ReplyKeyboardRemove()
    )
    
def settings_handler(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text = "Biz hozircha faqat O'zbek tilida ishlaymiz!⌨️"
    )
    bot.send_message(
        chat_id=user.id,
        text = "Yaqin kunlardan boshlab Inglis va Rus tili ham qo'shiladi!🌏"
    )
    
    
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
    