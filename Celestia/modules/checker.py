from pyrogram import Client, filters
import requests
from Celestia import Celestia


@Celestia.on_message(filters.command("start"))
def start_command(client, message):
    chat_id = message.chat.id
    username = message.from_user.username
    message_id = message.message_id
    client.send_message(
        chat_id,
        f"─ Switchblade Checker Panel ─\n⁕ Registered as ➞ @{username}\n⁕ Use ➞ /cmds to show available commands.\n⁕ Owner ➞ @pentagrvm | Update Logs ➞ @switchbladeupdate",
        reply_to_message_id=message_id
    )

@Celestia.on_message(filters.command("cmds"))
def cmds_command(client, message):
    chat_id = message.chat.id
    client.send_message(
        chat_id,
        "─ Switchblade Commands ─\n\n➣ Stripe Charge/Auth [✅]\nUsage: /chk cc|mm|yy|cvv\n\n➣ Check SK Key [✅]\nUsage: /key sk_live\n➣ Check Info [✅]\nUsage: /info\n➣ Check BIN Info [✅]\nUsage: /bin xxxxxx\nContact → @pentagrvm"
    )

@Celestia.on_message(filters.regex(r'^/(bin|!bin|\!bin|\.bin) (.+)$'))
def bin_check_command(client, message):
    chat_id = message.chat.id
    username = message.from_user.username
    message_id = message.message_id

    bin = message.matches[0].group(1)
    bin = bin[:6]

    response = requests.get(f"https://lookup.binlist.net/{bin}")
    data = response.json()

    bank = data.get("bank", {}).get("name", "")
    name = data.get("name", "")
    brand = data.get("brand", "")
    country = data.get("country", {}).get("name", "")
    scheme = data.get("scheme", "")
    emoji = data.get("emoji", "")
    card_type = data.get("type", "")

    message_text = f'⁕ ─ 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ✅ ─ ⁕\nBIN: {bin}\nBANK: {bank}\n𝙲𝙾𝚄𝙽𝚃𝚁𝚞: {name}  ({emoji})\nBRAND: {brand}\nCARD: {scheme}\nTYPE: {card_type}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nCHECKED BY: @{username}'

    client.send_message(
        chat_id,
        message_text,
        reply_to_message_id=message_id,
        parse_mode="html"
    )

@Celestia.on_message(filters.command(["info", "id"]))
def info_id_command(client, message):
    chat_id = message.chat.id
    username = message.from_user.username
    firstname = message.from_user.first_name

    if message.text == "/info":
        info_text = f"⁕ ─ 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 ─ ⁕\nChat ID: {chat_id}\nName: {firstname}\nUsername: @{username}"
    else:
        info_text = f"Chat ID: {chat_id}"

    client.send_message(
        chat_id,
        info_text,
        parse_mode="html"
    )





