from telegram import Update 
from telegram.ext import CallbackContext
from contact import contact_handler
from contact_en import contact_handler_en
from contact_ru import contact_handler_ru

def common_contact_handler(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    
    if lang == 'Uzbek 🇺🇿':
        return contact_handler(update, context)
    
    elif lang == 'English 🇺🇸':
        return contact_handler_en(update, context)
    
    elif lang == 'Русский 🇷🇺':
        return contact_handler_ru(update, context)