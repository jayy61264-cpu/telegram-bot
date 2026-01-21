from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8525781107:AAHCXsy6XdkTNRK2TPxLmzEVYD_zoaAKLZU"
OWNER_ID = 2097979865

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        name = update.effective_user.first_name
        username = update.effective_user.username
        text = update.message.text

        msg = f"📩 New message\n👤 {name} (@{username})\n\n{text}"
        await context.bot.send_message(chat_id=OWNER_ID, text=msg)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

print("Bot is running...")
app.run_polling()
