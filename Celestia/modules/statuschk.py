import os, re, pytz, asyncio, datetime
from pyrogram import filters
from pyrogram.errors import FloodWait
from config import SUDO_USERS 
from Celestia import Celestia, userbot

BOT_LIST = [5997219860, 6796545941]
MESSAGE_ID = [33]
GROUP_ID = [-1001802990747]
CHANNEL_ID = [-1001934794766]

async def main_status():
    async with userbot:
        while True:
            print("ᴄʜᴇᴄᴋɪɴɢ...")
            xxx_teletips = "<u>**🏷 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {chat_title} ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ**</u>\n\n 📈 | <u>**ʀᴇᴀʟ ᴛɪᴍᴇ ʙᴏᴛ's sᴛᴀᴛᴜs 🍂**</u>".format(chat_title="Your Chat Title")  # Replace "Your Chat Title" with the actual chat title.
            for bot in BOT_LIST:
                await asyncio.sleep(7)
                try:
                    bot_info = await userbot.get_users(bot)
                except Exception:
                    bot_info = bot

                try:
                    yyy_teletips = await userbot.send_message(bot, "/start")
                    aaa = yyy_teletips.id
                    await asyncio.sleep(15)
                    zzz_teletips = userbot.get_chat_history(bot, limit=1)
                    async for ccc in zzz_teletips:
                        bbb = ccc.id
                    if aaa == bbb:
                        xxx_teletips += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**"
                        for bot_admin_id in SUDO_USERS:
                            try:
                                await Celestia.send_message(int(GROUP_ID), f"**ᴋʏᴀ ᴋᴀʀ ʀᴀʜ ʜᴀɪ ʙʜᴀɪ, 😡\n[{bot_info.first_name}](tg://user?id={bot_info.id}) ʙᴀɴᴅ ᴘᴀᴅᴀ ʜᴀɪ ᴵ ᴡᴏʜ ᴛᴏʜ ᴀᴄᴄʜᴀ ʜᴜᴀ ᴍᴀɪɴᴇ ᴅᴇᴋʜ ʟɪʏᴀ**")
                            except Exception:
                                pass  # Handle this exception appropriately.
                        await app.read_chat_history(bot)
                    else:
                        xxx_teletips += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**"
                        await userbot.read_chat_history(bot)
                except FloodWait as e:
                    ttm = re.findall("\d{0,5}", str(e))
                    await asyncio.sleep(int(ttm))
            time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            last_update = time.strftime("%d %b %Y at %I:%M %p")
            xxx_teletips += f"\n\n✅ <u>ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ:</u>\n**ᴅᴀᴛᴇ & ᴛɪᴍᴇ: {last_update}**\n**ᴛɪᴍᴇ ᴢᴏɴᴇ: (Asia/Kolkata)**\n\n<i><u>♻️ ʀᴇғʀᴇsʜᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴡɪᴛʜɪɴ 4 ʜᴏᴜʀꜱ.</u></i>\n\n<i>**๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ sᴜᴍɪᴛ ʏᴀᴅᴀᴠ ๏**</i>"
            await userbot.edit_message_text(int(CHANNEL_ID), MESSAGE_ID, xxx_teletips)
            print(f"ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update}")
            await asyncio.sleep(14400)

userbot.run(main_status())



