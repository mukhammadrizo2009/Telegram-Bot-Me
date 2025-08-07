from telegram import Update
from telegram.ext import CallbackContext

def get_help(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Yordam so'rash uchun murojat qiling😊: https://muhammadrizomirzaev671@gmail.com" 
    )
    bot.send_message(
        chat_id = user.id,
        text = "Har qanday murojatni ko'rib chiqishga tayormiz!👍" 
    )