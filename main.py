from telegram.ext import ApplicationBuilder, CommandHandler
from config import Config
from commands.start import start_command

def main():
    if not Config.BOT_TOKEN:
        print("Error: BOT_TOKEN nahi mila!")
        return

    app = ApplicationBuilder().token(Config.BOT_TOKEN).build()

    # Commands folder se handler add karna
    app.add_handler(CommandHandler("start", start_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
