import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os
import openai

# ✅ OPENAI API KEY (GPT के लिए)
openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# ✅ Shayari, Caption, Bio, etc.
shayari_list = [
    "तेरे बिना अधूरी सी लगती है ज़िन्दगी ❤️",
    "हर पल तुझसे ही प्यार करते हैं 💞",
    "Attitude हमारा खतरनाक है 😎🔥"
]

captions_list = [
    "Smile. Sparkle. Shine ✨",
    "Born to express, not to impress 💫",
    "Self-love is the best love ❤️"
]

bio_list = [
    "📍Dreamer | Believer | Achiever",
    "💫 Creating my own sunshine",
    "🖤 Life is short. Make it sweet."
]

story_list = [
    "एक बार एक लड़का था जिसे सच्चा प्यार हुआ...",
    "उसे खोकर ही मुझे असली प्यार की क़ीमत समझ आई...",
    "उस दिन बारिश हो रही थी, और दिल भी रो रहा था..."
]

motivation_list = [
    "जो लोग खुद पर विश्वास करते हैं, वही दुनिया बदलते हैं 💪",
    "हर सुबह एक नई शुरुआत है 🌞"
]

# 🔹 START command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 नमस्ते! मैं @AjayMoreAi_bot हूँ!\n\nआप ये commands भेज सकते हैं:\n"
        "/shayari\n/caption\n/bio\n/hashtag\n/motivation\n/story\n/talk"
    )

# 🔹 SHAYARI
async def shayari(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(shayari_list))

# 🔹 CAPTION
async def caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(captions_list))

# 🔹 BIO
async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(bio_list))

# 🔹 MOTIVATION
async def motivation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(motivation_list))

# 🔹 STORY
async def story(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(story_list))

# 🔹 HASHTAG GENERATOR
async def hashtag(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("❌ उपयोग: /hashtag love, attitude, selfie")
        return
    topic = "_".join(args)
    hashtags = [f"#{topic}{i}" for i in range(1, 6)]
    await update.message.reply_text(" ".join(hashtags))

# 🔹 TALK (ChatGPT style reply)
async def talk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = " ".join(context.args)
    if not user_input:
        await update.message.reply_text("❌ कृपया कुछ लिखिए: `/talk तुम कैसी हो?`")
        return
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        text = response['choices'][0]['message']['content']
        await update.message.reply_text(text)
    except Exception as e:
        await update.message.reply_text(f"❌ GPT Error: {e}")

# 🔹 Main function
def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN") or "7638312232:AAFlLrMCApPVeihOB0MEm21wwqHTJThHn8Q"
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shayari", shayari))
    app.add_handler(CommandHandler("caption", caption))
    app.add_handler(CommandHandler("bio", bio))
    app.add_handler(CommandHandler("hashtag", hashtag))
    app.add_handler(CommandHandler("motivation", motivation))
    app.add_handler(CommandHandler("story", story))
    app.add_handler(CommandHandler("talk", talk))

    app.run_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
