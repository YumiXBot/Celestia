import asyncio
from pyrogram import filters
from Celestia import Celestia, userbot

BOT_LIST = ["CelestiaXBot", "ZuliAiBot", "KAYAMATMUSICBOT"]

@Celestia.on_message(filters.command("botschk"))
async def bots_chk(celestia, message):
    msg = await message.reply("Checking bot stats...")
    response = ""
    for bot_username in BOT_LIST:
        try:
            bot = await userbot.get_users(bot_username)
            bot_id = bot.id
            bot_info = await userbot.send_message(bot, "/start")
            bot_check = await userbot.get_chat_history(bot, limit=1)
            for bot_message in bot_check:
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **Status: Online ✨**\n"
                else:
                    response += f"╭⎋ {bot_username}\n╰⊚ **Status: Offline ❄**\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **Status: Error ❌**\n"
    
    await msg.edit_text(response)



