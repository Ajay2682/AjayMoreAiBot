import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Shayari / Caption list
shayari_list = [
    "💌 प्यार वो एहसास है जो लफ्जों में बयान नहीं होता...",
    "😎 Attitude: हम वहां खड़े होते हैं जहाँ मैटर बड़े होते हैं।",
    "📸 Caption: 'Smile more, worry less.'"
]

motivation_list = [
    "🧠 जो खो गया, उसके लिए रोया नहीं करते...",
    "🔥 खुद को कमजोर समझना सबसे बड़ा पाप है - स्वामी विवेकानंद"
]

hashtags = {
    "love": "#love #romance #feeling #instagood",
    "attitude": "#attitude #swag #style #boss",
    "sad": "#alone #sadlife #broken #tears"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to AjayMoreAi_bot!")
Use /shayari, /image, /hashtag, /download, /motivate")

async def shayari(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(shayari_list))

async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(motivation_list))

async def hashtag(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = ' '.join(context.args).lower()
    result = hashtags.get(topic, "#life #thoughts #dailyquotes")
    await update.message.reply_text(f"🏷️ Hashtags for '{topic}':
{result}")

async def image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🖼 AI Image Generator is under setup... (connect with Replicate API)")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⬇️ Video Downloader feature coming soon!")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shayari", shayari))
    app.add_handler(CommandHandler("motivate", motivate))
    app.add_handler(CommandHandler("hashtag", hashtag))
    app.add_handler(CommandHandler("image", image))
    app.add_handler(CommandHandler("download", download))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
