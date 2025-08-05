from config import TOKEN
from telegram.ext import Updater , MessageHandler , Filters , CommandHandler 
from handlers import start , my_order , contact_handler , remove_keyboard , menu_handler ,settings_handler , our_info , send_idea


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    # CommandHandler
    dispatcher.add_handler(CommandHandler('start' , start))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.text("📦 Buyurtmalarim!"), my_order))
    dispatcher.add_handler(MessageHandler(Filters.text("🤕 Dasturni tark etish!") , remove_keyboard))
    dispatcher.add_handler(MessageHandler(Filters.text("⬅️ Orqaga qaytish!") , menu_handler))
    dispatcher.add_handler(MessageHandler(Filters.text("⚙️ Sozlamalar!"), settings_handler))
    dispatcher.add_handler(MessageHandler(Filters.text("ℹ️ Biz haqimizda!") , our_info))
    dispatcher.add_handler(MessageHandler(Filters.text("✍️ Fikr qoldirish!") , send_idea))
    
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
