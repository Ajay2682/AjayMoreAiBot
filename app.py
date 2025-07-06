import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# ✅ Tokens अब सुरक्षित तरीके से लिए जा रहे हैं
BOT_TOKEN = os.getenv("BOT_TOKEN")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

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
    await update.message.reply_text("👋 Welcome to AjayMoreAi_bot!\nUse /shayari, /image, /hashtag, /motivate")

async def shayari(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(shayari_list))

async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(motivation_list))

async def hashtag(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = ' '.join(context.args).lower()
    result = hashtags.get(topic, "#life #thoughts #dailyquotes")
    await update.message.reply_text(f"🏷️ Hashtags for '{topic}':\n{result}")

async def image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = ' '.join(context.args)
    if not prompt:
        await update.message.reply_text("🎨 कृपया image के लिए कोई prompt दो।\nउदाहरण: /image girl walking in forest")
        return
    await update.message.reply_text(f"🖼 Image Generator Active soon...\nPrompt: {prompt}")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⬇️ Video Downloader feature जल्द आ रहा है...")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
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
