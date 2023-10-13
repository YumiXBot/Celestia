import requests
import openai
import random
from config import SUDO_USERS, OWNER_ID
from Celestia import *
from pyrogram import * 
from pyrogram.types import *
from Celestia.Helper.database import *
from pyrogram.enums import ChatMemberStatus, ChatType
from Celestia.Helper.cust_p_filters import admin_filter






hiroko_text = [
"hey please don't disturb me.",
"who are you",    
"aap kon ho",
"aap mere owner to nhi lgte ",
"hey tum mera name kyu le rhe ho meko sone do",
"ha bolo kya kaam hai ",
"dekho abhi mai busy hu ",
"hey i am busy",
"aapko smj nhi aata kya ",
"leave me alone",
"dude what happend",    
]

strict_txt = [
"i can't restrict against my besties",
"are you serious i am not restrict to my friends",
"fuck you bsdk k mai apne dosto ko kyu kru",
"hey stupid admin ", 
"ha ye phele krlo maar lo ek dusre ki gwaand",  
"i can't hi is my closest friend",
"i love him please don't restict this user try to usertand "
]


# ========================================= #


def main(prompt: str) -> str:
    client = Client()
    response = client.palm(prompt)
    return response["content"].strip()


# ========================================= #


api_key = "BLUE-AI-25154789-6280048819-123-white-kazu-6280048819"

def get_response(user_id, query):
    params = {
        "user_id": user_id,
        "query": query,
        "BOT_ID": 5997219860
    }

    headers = {
        "api_key": api_key
        
    }

    response = requests.get("https://blue-api.vercel.app/chatbot1", params=params, headers=headers)
    return response.json()



# ========================================= #

openai.api_key = "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"

completion = openai.Completion()

start_sequence = "\nCelestia:"
restart_sequence = "\nPerson:"
session_prompt = chatbot_txt
session = {}

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'


# ========================================= #






@Celestia.on_message(filters.text, group=200)
async def chatbot_reply(celestia: Celestia, message):
    bot_id = 5997219860
    reply = message.reply_to_message
    if reply and reply.from_user.id == bot_id:
        query = message.text
        try:
            chat_log = session.get('chat_log')
            answer = ask(query, chat_log)
            session['chat_log'] = append_interaction_to_chat_log(Message, answer, chat_log)
            await message.reply(str(answer), quote=True)
        except Exception as e:
            print(f"Error: {e}")
            try:
                response = main(query)
                return await message.reply(response) 
            except Exception as e:
                print(f"Error: {e}")
                try:               
                    response = get_response(message.from_user.id, query)
                    await message.reply_text(response["result"]["text"])
                except Exception as e:
                    print(f"Error: {e}")



# ========================================= #


ban = ["ban","boom"]
unban = ["unban",]
mute = ["mute","silent","shut"]
unmute = ["unmute","speak","free"]
kick = ["kick", "out","nikaal"]
promote = ["promote","update"]
demote = ["demote"]




# ========================================= #

@Celestia.on_message(filters.command("elestia", prefixes=["c", "C"]) & admin_filter)
async def restriction_celestia(celestia: Celestia, message):
    chat_id = message.chat.id
    text = message.text.split(maxsplit=1)[1]
    data = text.split()

    if len(data) < 2:
        return await message.reply(random.choice(hiroko_text))

    reply = message.reply_to_message
    user_id = reply.from_user.id if reply else None

    # Check if the bot has permissions to ban, kick, mute, etc.
    bot_permissions = await celestia.get_chat_member(chat_id, celestia.me.id)
    if not bot_permissions.can_restrict_members:
        return await message.reply("I don't have the required permissions to perform these actions.")

    admin_check = await celestia.get_chat_member(chat_id, message.from_user.id)
    if not admin_check.privileges.can_restrict_members:
        return await message.reply("You don't have the necessary permissions to perform these actions.")

    for action in data[1:]:
        print(f"present {action}")

        if user_id is None:
            if action.startswith('@'):
                username = action[1:]
                user = await celestia.get_users(username)
                if user:
                    user_id = user.id

        if action in ban:
            if user_id:
                try:
                    await celestia.ban_chat_member(chat_id, user_id)
                    await message.reply("OK, banned!")
                except Exception as e:
                    await message.reply(f"Failed to ban the user: {e}")

        # ... (other actions)

        if action in unmute:
            if user_id:
                try:
                    permissions = ChatPermissions(can_send_messages=True)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply("Huh, OK, sir!")
                except Exception as e:
                    await message.reply(f"Failed to unmute the user: {e}")








"""
@Celestia.on_message(filters.command("elestia", prefixes=["c", "C"]) & admin_filter)
async def restriction_celestia(celestia: Celestia, message):
    chat_id = message.chat.id
    text = message.text.split(maxsplit=1)[1]
    data = text.split()
    
    if len(data) < 1:
        return await message.reply(random.choice(hiroko_text))
    
    reply = message.reply_to_message
    user_id = reply.from_user.id if reply else None

    for action in data:
        print(f"present {action}")
        
        if action in ban:
            if user_id:
                if user_id in SUDO_USERS:
                    await message.reply(random.choice(strict_txt))
                else:
                    await celestia.ban_chat_member(chat_id, user_id)
                    await message.reply("OK, banned!")
        
        if action in unban:
            if user_id:
                await celestia.unban_chat_member(chat_id, user_id)
                await message.reply("OK, unbanned!")
        
        if action in kick:
            if user_id:
                if user_id in SUDO_USERS:
                    await message.reply(random.choice(strict_txt))
                else:
                    await celestia.ban_chat_member(chat_id, user_id)
                    await celestia.unban_chat_member(chat_id, user_id)
                    await message.reply("Get lost! Bhag diya bhosdi wale ko")
        
        if action in mute:
            if user_id:
                if user_id in SUDO_USERS:
                    await message.reply(random.choice(strict_txt))
                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply("Muted successfully! Disgusting people.")
        
        if action in unmute:
            if user_id:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply("Huh, OK, sir!")







 
@Celestia.on_message(filters.command("elestia", prefixes=["c", "C"]) & filters.user(OWNER_ID))
async def assist_celestia(celestia: Celestia, message):
    text = message.text.split(maxsplit=1)[1]
    data = text.split()

    for item in data:
        item_lower = item.lower()

        if "group" in item_lower:
            chat = await userbot.create_group("Group Title", 5997219860)
            chat_id = chat.id
            link = await userbot.export_chat_invite_link(chat_id)
            await celestia.send_message(message.chat.id, text=f"Here is your group link: {link}")

        if "channel" in item_lower:
            chat = await userbot.create_channel("Channel", "No description")
            chat_id = chat.id
            link = await userbot.export_chat_invite_link(chat_id)
            await celestia.send_message(message.chat.id, text=f"Here is your channel link: {link}")

"""
