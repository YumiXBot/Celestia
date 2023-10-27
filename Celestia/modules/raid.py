import asyncio, random, asyncio, time
from typing import Tuple
from traceback import format_exc
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters
from Celestia import Celestia
from config import SUDO_USERS, OWNER_ID



GROUPS = []


ACTIVATE_LIST = []

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])





@Celestia.on_message(filters.user(SUDO_USERS) & filters.command(["replyraid", "rraid"], [".", "!"]))
async def gban(celestia, message):
    celu = await message.reply_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await celu.edit("**Whome should I replyraid?**")
            return
    get_user = await celestia.get_users(user)
    if int(message.chat.id) in GROUP:
        await sex.edit("`Baap Ke Group Me Spam Nahi!`")
        return
    if int(get_user.id) in OWNER_ID:
        await celu.edit("Chal Chal baap Ko mat sikha")
        return
    elif int(get_user.id) in SUDO_USERS:
        await celu.edit("Abe Lawde that guy part of my sudo users.")
        return
    elif int(get_user.id) in ACTIVATE_LIST:
        await celu.edit("Already raid activate in this user.")
        return
    ACTIVATE_LIST.append(get_user.id)
    await celu.edit(f"**Successfully Reply Raid Started {get_user.first_name}!**")



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dreplyraid", "drraid"], [".", "!"]))
async def gbam(celestia, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.reply_text("**Whome should I dreplyraid?**")
            return
    get_user = await celestia.get_users(user)
    ACTIVATE_LIST.remove(get_user.id)
    await message.reply_text(f"**Reply Raid has Been Removed {get_user.first_name}, enjoy!**")


@Celestia.on_message(filters.all)
async def check_and_del(celestia, message):
    if not message:
        return
    if int(message.chat.id) in GROUPS:
        return
    try:
        if not message.from_user.id in ACTIVATE_LIST:
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await message.reply_text(f"{random.choice(RAID)}")
    except:
        pass




  
