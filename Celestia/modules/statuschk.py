import os
import re
import pytz
import asyncio
import datetime
import config
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from config import GROUP_ID, CHANNEL_OR_GROUP_ID, MESSAGE_ID, CHANNEL_NAME, TIME_ZONE, BOT_LIST, BOT_ADMIN_IDS





app = Client(
    name = "sumit",
    api_id = config.API_ID,
    api_hash = config.API_HASH,
    session_string = config.SESSION_STRING
)


async def main_status():
    async with app:
            while True:
                print("ᴄʜᴇᴄᴋɪɴɢ...")
                xxx_teletips = f"<u>**🏷 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {CHANNEL_NAME} ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ**</u>\n\n 📈 | <u>**ʀᴇᴀʟ ᴛɪᴍᴇ ʙᴏᴛ's sᴛᴀᴛᴜs 🍂**</u>"
                for bot in BOT_LIST:
                    await asyncio.sleep(7)
                    try:
                        bot_info = await app.get_users(bot)
                    except Exception:
                        bot_info = bot

                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(15)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(GROUP_ID), f"**ᴋʏᴀ ᴋᴀʀ ʀᴀʜᴀ ʜᴀɪ ʙʜᴀɪ, 😡\n[{bot_info.first_name}](tg://user?id={bot_info.id}) ʙᴀɴᴅ ᴘᴀᴅᴀ ʜᴀɪ ᴡᴏʜ ᴛᴏʜ ᴀᴄᴄʜᴀ ʜᴜᴀ ᴍᴀɪɴᴇ ᴅᴇᴋʜ ʟɪʏᴀ**")
                                except Exception:...
                            await app.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        ttm = re.findall("\d{0,5}", str(e))
                        await asyncio.sleep(int(ttm))
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += f"\n\n✅ <u>ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ:</u>\n**ᴅᴀᴛᴇ & ᴛɪᴍᴇ: {last_update}**\n**ᴛɪᴍᴇ ᴢᴏɴᴇ: ({TIME_ZONE})**\n\n<i><u>♻️ ʀᴇғʀᴇsʜᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴡɪᴛʜɪɴ 4 ʜᴏᴜʀꜱ.</u></i>\n\n<i>**๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ sᴜᴍɪᴛ ʏᴀᴅᴀᴠ ๏**</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update}")                
                await asyncio.sleep(14400)
                        
app.run(main_status())



