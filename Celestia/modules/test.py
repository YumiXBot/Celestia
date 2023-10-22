import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Celestia import Celestia, userbot

BOT_LIST = [5997219860, 6796545941]  # List of bot user IDs to check

@Celestia.on_message(filters.command("botstats", prefixes="/"))
async def bot_stats(_, message: Message):
    async def check_bot_status(bot_id):
        try:
            bot_message = await userbot.send_message(bot_id, "/start")
            await asyncio.sleep(5)  # Adjust this delay based on how long it takes for your bots to respond.
            if bot_message and bot_message.text:
                return f"Bot {bot_id}: Alive"
            else:
                return f"Bot {bot_id}: Dead"
        except Exception:
            return f"Bot {bot_id}: Dead"

    statuses = await asyncio.gather(*(check_bot_status(bot_id) for bot_id in BOT_LIST))
    response = "\n".join(statuses)
    await message.reply(response)



