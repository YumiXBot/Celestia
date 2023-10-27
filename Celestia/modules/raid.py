import random
from pyrogram import filters
from Celestia import Celestia
from config import SUDO_USERS, OWNER_ID
from Celestia.Helper.database.raiddb import GROUPS, RAID

ACTIVATE_LIST = []


def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@Celestia.on_message(filters.user(SUDO_USERS) & filters.command(["replyraid", "rraid"], [".", "!"]))
async def replyraid(celestia, message):
    celu = await message.reply_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user.id
    else:
        user = get_arg(message)
        if not user:
            await celu.edit("**Whom should I replyraid?**")
            return
    get_user = await celestia.get_users(user)
    if int(message.chat.id) in GROUPS:
        await celu.edit("`Abe bsdk sale mere group me mujhse hi spam krwayega!`")
        return
    if int(get_user.id) in OWNER_ID:
        await celu.edit("Wew, ye to mere pati dev hai.")
        return
    elif int(get_user.id) in SUDO_USERS:
        await celu.edit("Abe Lawde, ye to mere dost hai.")
        return
    elif int(get_user.id) in ACTIVATE_LIST:
        await celu.edit("Already raid activated for this user.")
        return
    ACTIVATE_LIST.append(get_user.id)
    await celu.edit(f"**Successfully Reply Raid Started for {get_user.first_name}!**")


@Celestia.on_message(filters.user(SUDO_USERS) & filters.command(["dreplyraid", "drraid"], [".", "!"]))
async def removeraid(celestia, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user.id
    else:
        user = get_arg(message)
        if not user:
            await message.reply_text("**Whom should I dreplyraid?**")
            return
    get_user = await celestia.get_users(user)
    ACTIVATE_LIST.remove(get_user.id)
    await message.reply_text(f"**Reply Raid has Been Removed for {get_user.first_name}, enjoy!**")



@Celestia.on_message(filters.all)
async def check_and_del(celestia, message):
    if not message:
        return
    if int(message.chat.id) in GROUPS:
        return
    try:
        if message.from_user.id not in ACTIVATE_LIST:
            return
    except AttributeError:
        return
    try:
        await message.reply_text(f"{random.choice(RAID)}")
    except Exception as e:
        print(f"An error occurred: {e}")





