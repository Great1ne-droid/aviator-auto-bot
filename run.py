from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from aviator_bot import send_prediction_signal, send_skip_signal
from config import low_threshold, min_safe_multiplier, min_lows_before_entry

async def crash(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        values = [float(x) for x in context.args]
        if len(values) != 5:
            await update.message.reply_text("❗ Please enter exactly 5 crash values like this:\n/crash 1.00 1.20 1.30 1.00 1.00")
            return

        low_count = sum(1 for x in values if x < low_threshold)

        if low_count >= min_lows_before_entry:
            send_prediction_signal(values[-1], min_safe_multiplier)
        else:
            send_skip_signal(values[-1])

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")

if __name__ == '__main__':
    from config import BOT_TOKEN
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("crash", crash))
    print("🤖 Bot is live on Render...")
    app.run_polling()
