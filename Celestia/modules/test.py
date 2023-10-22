import os, re, pytz, asyncio, datetime
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from config import SUDO_USERS
from Celestia import Celestia, userbot

BOT_LIST = [5997219860, 6796545941]
GROUP_ID = -1001802990747
CHANNEL_ID = -1001934794766

@Celestia.on_message(filters.command("botstats") & filters.user(SUDO_USERS))
async def bot_status_command(_, message):
    online_bots = []
    offline_bots = []
    for bot_id in BOT_LIST:
        try:
            bot_info = await userbot.get_users(bot_id)
            await asyncio.sleep(7)
            yyy_teletips = await userbot.send_message(bot_id, "/start")
            await asyncio.sleep(15)
            zzz_teletips = await userbot.get_chat_history(bot_id, limit=1)
            async for ccc in zzz_teletips:
                if yyy_teletips.message_id == ccc.message_id:
                    offline_bots.append(bot_info.first_name)
                else:
                    online_bots.append(bot_info.first_name)
        except FloodWait as e:
            ttm = re.findall("\d{0,5}", str(e))
            await asyncio.sleep(int(ttm))

    online_bots_text = "\n".join([f"✅ {bot_name}" for bot_name in online_bots])
    offline_bots_text = "\n".join([f"❌ {bot_name}" for bot_name in offline_bots])
    message_text = f"**Online Bots:**\n{online_bots_text}\n\n**Offline Bots:**\n{offline_bots_text}"
    await message.reply_text(message_text)

async def main_status():
    async with userbot:
        await Celestia.start()
        await userbot.send_message(GROUP_ID, "Bot is online and ready!")


    asyncio.get_event_loop().run_until_complete(main_status())



