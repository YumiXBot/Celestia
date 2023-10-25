import asyncio
from pyrogram import filters
from Celestia import Celestia, userbot

BOT_LIST = ["CelestiaXBot", "ZuliAiBot", "KAYAMATMUSICBOT"]  


@Celestia.on_message(filters.command("botschk"))
async def bots_chk(celestia, message):
    alive_bots = []
    dead_bots = []

    for bot_username in BOT_LIST:
        try:
            bot_info = await userbot.get_users(bot_username)
            alive_bots.append(bot_info)
        except Exception:
            dead_bots.append(bot_username)

    alive_msg = "\n".join(f"╭⎋ [{bot.first_name}](tg://user?id={bot.id}) \n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**" for bot in alive_bots)
    dead_msg = "\n".join(f"╭⎋ {bot_username} \n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**" for bot_username in dead_bots)

    response = "Bots list with live:\n" + alive_msg if alive_bots else "All bots are dead.\n" + dead_msg
    await message.reply_text(response)



