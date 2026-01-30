import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8318110132:AAHaIakWzG3zhzoqWXyA4s6T5E7x0ph_4V0"

AMAZON_TAG = "akash-21"
#FLIPKART_ID = "YOURID"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 Welcome!\n\nType a product name to search on Amazon & Flipkart.\n\nExample: iPhone 14"
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.replace(" ", "+")

    amazon_link = f"https://www.amazon.in/s?k={query}&tag={AMAZON_TAG}"
   # flipkart_link = f"https://www.flipkart.com/search?q={query}&affid={FLIPKART_ID}"

    keyboard = [
        [InlineKeyboardButton("🟧 Buy on Amazon", url=amazon_link)],
        #[InlineKeyboardButton("🟦 Buy on Flipkart", url=flipkart_link)]
    ]

    await update.message.reply_text(
        f"🔍 Results for: *{update.message.text}*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

app.run_polling()
