import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("8318110132:AAHzuRX8LqezVrj14We88ZXawhDorkQ6YYI")
AMAZON_TAG = "akash-21"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 Welcome to Amazon Shopping Bot!\n\n"
        "Send any product name to get an Amazon link.\n"
        "Example: iPhone 14"
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.replace(" ", "+")
    link = f"https://www.amazon.in/s?k={query}&tag={AMAZON_TAG}"

    keyboard = [[InlineKeyboardButton("🟧 Buy on Amazon", url=link)]]

    await update.message.reply_text(
        f"🔍 Results for: {update.message.text}",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    app.run_polling()

if __name__ == "__main__":
    main()
