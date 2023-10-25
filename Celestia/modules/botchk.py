import asyncio
from pyrogram import filters
from Celestia import Celestia, userbot


@Celestia.on_message(filters.command("botschk"))
async def bots_chk(celestia, message):
  for bot in BOT_LIST:
    try:
      bot_info = await userbot.get_users(bot)
    except Exception:
      bot_info = bot
      try:
        await asyncio.sleep(0.2)
        bots_chk = await userbot.send_message(bot, "/start")
        celu = bots_chk.id
        async for cele in bots_chk:
        bots_chk = userbot.get_chat_history(bot, limit = 1)
        if celu == cele:
                            bots_chk += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**"
                            
                            await userbot.read_chat_history(bot)
                        else:
                            bots_chk += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**"
                            await userbot.read_chat_history(bot)





