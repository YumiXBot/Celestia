import os
import re
import pytz
import asyncio
import datetime
from pyrogram import filters
from pyrogram.errors import FloodWait
from config import SUDO_USERS 
from Celestia import Celestia, userbot

BOT_LIST = [5997219860, 6796545941]
MESSAGE_ID = 33
GROUP_ID = -1001802990747
CHANNEL_ID = -1001934794766

async def check_bot_status(bot_id):
    try:
        bot_info = await userbot.get_users(bot_id)
        yyy_teletips = await userbot.send_message(bot_id, "/start")
        aaa = yyy_teletips.message_id
        await asyncio.sleep(15)
        zzz_teletips = await userbot.get_chat_history(bot_id, limit=1)
        async for ccc in zzz_teletips:
            bbb = ccc.message_id
        if aaa == bbb:
            return f"{bot_info.first_name}: offline"
        else:
            return f"{bot_info.first_name}: online"
    except FloodWait as e:
        ttm = re.findall(r"\d{0,5}", str(e))
        await asyncio.sleep(int(ttm[0]))
        return f"FloodWait: {ttm[0]} seconds"
    except Exception as e:
        return f"Error: {e}"

async def main_status():
    async with userbot:
        await Celestia.start()
        await Celestia.send_message(GROUP_ID, "stats checking started")
        while True:
            print("ᴄʜᴇᴄᴋɪɴɢ...")
            status_messages = await asyncio.gather(*(check_bot_status(bot_id) for bot_id in BOT_LIST))
            xxx_teletips = "<u>**🏷 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ Your Chat Title ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ**</u>\n\n 📈 | <u>**ʀᴇᴀʟ ᴛɪᴍᴇ ʙᴏᴛ's sᴛᴀᴛᴜs 🍂**</u>"
            for status in status_messages:
                xxx_teletips += f"\n\n{status}"
            time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            last_update = time.strftime("%d %b %Y at %I:%M %p")
            xxx_teletips += f"\n\n✅ <u>ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ:</u>\n**ᴅᴀᴛᴇ & ᴛɪᴍᴇ: {last_update}**\n**ᴛɪᴍᴇ ᴢᴏɴᴇ: (Asia/Kolkata)**\n\n<i><u>♻️ ʀᴇғʀᴇsʜᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴡɪᴛʜɪɴ 4 ʜᴏᴜʀꜱ.</u></i>\n\n<i>**๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ sᴜᴍɪᴛ ʏᴀᴅᴀᴠ ๏**</i>"
            await userbot.edit_message_text(CHANNEL_ID, MESSAGE_ID, xxx_teletips)
            print(f"ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update}")
            await asyncio.sleep(14400)


    try:
        asyncio.run(main_status())
    except Exception as e:
        print(f"Error: {e}")



