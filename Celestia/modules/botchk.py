import asyncio
from pyrogram import filters
from Celestia import Celestia, userbot
from config import SUDO_USERS

BOT_LIST = ["CelestiaXBot", "ZuliAiBot", "KAYAMATMUSICBOT"]



@Celestia.on_message(filters.command("botschk") & filters.user(SUDO_USERS))
async def bots_chk(celestia, message):
    msg = await message.reply("Checking bot stats...")
    response = ""
    for bot_username in BOT_LIST:
        try:
            bot = await userbot.get_users(bot_username)
            bot_id = bot.id
            bot_info = await userbot.send_message(bot, "/start")
            async for bot_message in userbot.get_chat_history(bot, limit=1):
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **Status: Online ✨**\n\n"
                else:
                    response += f"╭⎋ {bot_username}\n╰⊚ **Status: Offline ❄**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **Status: Error ❌**\n"
    
    await msg.edit_text(response)




