import logging
import asyncio
import signal
from pyrogram import Client, filters, idle
from pyrogram.errors import PeerIdInvalid, ChatWriteForbidden, FloodWait
from config import Config, CHANNEL_MAPPING
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Logging Setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Media Forward Bot Class
class MediaForwardBot(Client):
    def __init__(self):
        super().__init__(
            name="MediaForwardBot",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=10
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        logger.info(f"Bot started as {me.first_name} (@{me.username})")

    async def stop(self):
        await super().stop()
        logger.info("Bot stopped.")

# Initialize Bot
bot = MediaForwardBot()

# Allowed MIME Types for Filtering Videos
ALLOWED_MIME_TYPES = {"video/x-matroska", "video/mp4"}

# Safe Copy Function with Retry Logic
async def safe_copy(message, destination, retries=3):
    for attempt in range(retries):
        try:
            await message.copy(destination)
            return True  # Forwarding successful
        except FloodWait as e:
            logger.warning(f"FloodWait detected. Waiting {e.value} seconds before retrying.")
            await asyncio.sleep(e.value)
        except ChatWriteForbidden:
            logger.error(f"Bot cannot write to destination: {destination}. Check permissions.")
            return False  # Stop retrying on this error
        except PeerIdInvalid:
            logger.error(f"Invalid peer ID for destination: {destination}. Check configuration.")
            return False  # Stop retrying on this error
        except Exception as e:
            logger.error(f"Unexpected error while forwarding: {e}")
            return False  # Stop retrying on unexpected errors
    logger.error(f"Failed to forward message after {retries} retries.")
    return False

# Media Filtering Handler
@bot.on_message(filters.channel & filters.video)
async def forward_media(client, message):
    if message.video and message.video.mime_type in ALLOWED_MIME_TYPES:
        destination = CHANNEL_MAPPING.get(message.chat.id)
        if destination:
            await asyncio.sleep(1)  # Delay to reduce RANDOM_ID_DUPLICATE warnings
            success = await safe_copy(message, destination)
            if success:
                logger.info(f"Forwarded video from {message.chat.id} to {destination}")

# Graceful Shutdown Handler
async def main():
    try:
        await bot.start()
        logger.info("Bot is running...")
        await idle()  # Wait until a signal (e.g., Ctrl+C) is received
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        logger.info("Stopping bot...")
        await bot.stop()
        logger.info("Bot stopped successfully.")

if __name__ == "__main__":
    # Signal Handling for Graceful Shutdown
    loop = asyncio.get_event_loop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda: asyncio.ensure_future(bot.stop()))

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
