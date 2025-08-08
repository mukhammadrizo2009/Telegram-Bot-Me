from config import TOKEN
from telegram.ext import Updater , MessageHandler , Filters , CommandHandler 
from handlers import my_order, remove_keyboard , menu_handler ,settings_handler , our_info , send_idea
from start import start
from help import get_help
from contact import contact , contact_handler
from contact_en import contact_en , contact_handler_en
from my_order import my_order_en
from menu_en import remove_keyboard_en , menu_handler_en , our_info_en , send_idea_en , settings_handler_en
from contact_ru import contact_ru , contact_handler_ru
from moy_zakas import my_order_ru
from menu_ru import remove_keyboard_ru , menu_handler_ru , our_info_ru , send_idea_ru , settings_handler_ru



def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    # Command Handler
    dispatcher.add_handler(CommandHandler('start' , start))
    dispatcher.add_handler(CommandHandler('help' , get_help))
    dispatcher.add_handler(CommandHandler("stop" , remove_keyboard))
    
    # With Uzbek
    dispatcher.add_handler(MessageHandler(Filters.text("Uzbek 🇺🇿"), contact))
    dispatcher.add_handler(MessageHandler(Filters.contact , contact_handler )) 
    dispatcher.add_handler(MessageHandler(Filters.text("📦 Buyurtmalarim!"), my_order))
    dispatcher.add_handler(MessageHandler(Filters.text("🤕 Dasturni tark etish!") , remove_keyboard))
    dispatcher.add_handler(MessageHandler(Filters.text("⬅️ Orqaga qaytish!") , menu_handler))
    dispatcher.add_handler(MessageHandler(Filters.text("⚙️ Sozlamalar!"), settings_handler))
    dispatcher.add_handler(MessageHandler(Filters.text("ℹ️ Biz haqimizda!") , our_info))
    dispatcher.add_handler(MessageHandler(Filters.text("✍️ Fikr qoldirish!") , send_idea))
    
    # With English
    dispatcher.add_handler(MessageHandler(Filters.text("English 🇺🇸"), contact_en))
    dispatcher.add_handler(MessageHandler(Filters.contact , contact_handler_en ))
    dispatcher.add_handler(MessageHandler(Filters.text("📦 My orders!"), my_order_en))
    dispatcher.add_handler(MessageHandler(Filters.text("🤕 Exit the program!") , remove_keyboard_en))
    dispatcher.add_handler(MessageHandler(Filters.text("⬅️ Go back!") , menu_handler_en))
    dispatcher.add_handler(MessageHandler(Filters.text("⚙️ Settings!"), settings_handler_en))
    dispatcher.add_handler(MessageHandler(Filters.text("ℹ️ about Us!") , our_info_en))
    dispatcher.add_handler(MessageHandler(Filters.text("✍️ Send a comment!") , send_idea_en))
    
    # With Russian
    dispatcher.add_handler(MessageHandler(Filters.text("Русский 🇷🇺"), contact_ru))
    dispatcher.add_handler(MessageHandler(Filters.contact , contact_handler_ru ))
    dispatcher.add_handler(MessageHandler(Filters.text("📦 Мои заказы!"), my_order_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("🤕 Выйти из программы!") , remove_keyboard_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("⬅️ Возвращаться!") , menu_handler_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("⚙️ Настройки!"), settings_handler_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("ℹ️ О нас!") , our_info_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("✍️ Отправить комментарий!") , send_idea_ru))
    
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
