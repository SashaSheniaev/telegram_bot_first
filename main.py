from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes 


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('привіт як справи?')
    
    
def main():
    application = ApplicationBuilder().token('7715955682:AAGfZAcB5mH4RwbgfvshsO9wkBZhKrJOEj8').build()
    application.add_handler(CommandHandler('start',start))
    print('bot_starting')
    application.run_polling()
    
if __name__ == '__main__':
    main()
    