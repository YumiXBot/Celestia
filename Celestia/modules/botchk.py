import asyncio
from pyrogram import filters
from Celestia import Celestia, userbot

BOT_LIST = ["CelestiaXBot", "ZuliAiBot", "KAYAMATMUSICBOT"]

@Celestia.on_message(filters.command("botschk"))
async def bots_chk(celestia, message):
    msg = await message.reply("Checking bot stats...")
    response = ""
    for bot_username in BOT_LIST:
        await asyncio.sleep(0.5)
        try:
            bot = await userbot.get_users(bot_username)
            bot_id = bot.id
            await asyncio.sleep(0.5)
            bot_info = await userbot.send_message(bot_id, "/start")
            await asyncio.sleep(3)
            bot_check = await userbot.get_chat_history(bot_id, limit=1)
            for bot_message in bot_check:
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **Status: Online ✨**\n\n"
                else:
                    response += f"╭⎋ {bot_username}\n╰⊚ **Status: Offline ❄**\n\n"
        except Exception as e:
            response += f"╭⎋ {bot_username}\n╰⊚ **Status: Error {e} ❌**\n\n"
    
    await msg.edit_text(response)



