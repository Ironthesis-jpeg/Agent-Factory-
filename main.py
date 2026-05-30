# from thirdweb import ThirdwebSDK  # disabled for now    # HUB 5: THIRDWEB - Deploy token if yes

    # Placeholder response for now
    await update.message.reply_text(f"Done. {bot_name} is live.\n\nRepo: github.com/your_org/{bot_name.lower()}\nBot: t.me/{bot_name}Bot\nSite: {bot_name.lower()}.vercel.app\nToken: Coming soon")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Agent Factory live. Run /build to create your agent + token + site.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TG_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("build", build))
    print("Agent Factory bot is running")
    app.run_polling()
