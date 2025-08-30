import os
import random
import time
import telebot

# Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
# Channel ya Group username ( @ ke sath ) ya ID
CHANNEL_ID = os.getenv("CHANNEL_ID", "@YourChannelUsername")

bot = telebot.TeleBot(BOT_TOKEN)

# Signals list
signals = [
    """🧚🔤🔤🔤🔤🔤
💬💬💬💬💬💬💬💬
🕯Set - USD/MXN (OTC) 🎮
🔜Time Frame - 1Min (Default)⭐️
💬💬💬💬💬💬💬💬

🇪🇺PARUL SHOT🇪🇺"""
]

# Sticker list
stickers = [
    "CAACAgUAAxkBAAEM1ZVnhJvK...",  # Sticker 1 file_id
    "CAACAgUAAxkBAAEM1ZdnhJwq...",  # Sticker 2 file_id
    "CAACAgUAAxkBAAEM1ZlnhJw2...",  # Sticker 3 file_id
    "CAACAgUAAxkBAAEM1ZtnhJw9..."   # Sticker 4 file_id
]

print("✅ Bot started... Sending signals every 30 sec.")

while True:
    try:
        # Random signal
        signal = random.choice(signals)
        bot.send_message(CHANNEL_ID, signal)

        # Random sticker
        sticker = random.choice(stickers)
        bot.send_sticker(CHANNEL_ID, sticker)

    except Exception as e:
        print(f"⚠️ Error: {e}")

    time.sleep(30)
