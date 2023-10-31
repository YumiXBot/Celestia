import random
from Celestia import Celestia
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])




user_database = {}

user_family = {}

user_state = {}



@Celestia.on_message(filters.command("character"))
def character_creation(client, message):
    user_id = message.from_user.id

    if user_id in user_database:
        client.send_message(message.chat.id, "You have already chosen a character.")
        return

    character_name = " ".join(message.command[1:])
    if character_name:
        user_database[user_id] = {
            "name": character_name,
            "health": 100,
            "rank": "Novice Traveler",
            "partner": None,
            "experience": "[▰▱▱▱▱]",
            "level": 1,
            "celeus": 10000,
            "location": None,
            "battle_win": 0,
            "total_win": 0,
            "player_id": user_id
        }
        user_state[user_id] = "character_created"
        client.send_photo(message.chat.id, photo="https://telegra.ph/file/55e27bacddf487d920a1a.jpg", caption=f"Character {character_name} created! You can now use the /fight command.")



@Celestia.on_message(filters.command("profile", prefixes="/"))
def profile_command(client, message):
    user_id = message.from_user.id

    if user_id not in user_database:
        client.send_message(message.chat.id, "You haven't created a character yet. Use the /character command to create one.")
        return

    character_data = user_database[user_id]
    user_profile = f"""
┏━━━━━━━━━━━━━━━━━
┣ Umm Player profile 
┗━━━━━━━━━━━━━━━━━
┏━⦿
┣⬢ Name : {character_data['name']}
┣⬢ Health : {character_data['health']}
┣⬢ Celeus : {character_data['celeus']}
┣⬢ Player ID : {character_data['player_id']}
┗━━━━━━━━━⦿

┏━⦿
┣ Exp : {character_data['experience']}
┣ Level : {character_data['level']}
┣ Rank : {character_data['rank']}
┣ Location : {character_data['location']}
┣ Battles Win : {character_data['battle_win']}
┣ Total Battles : {character_data['total_win']}
┗━━━━━━━━━⦿
"""

    client.send_photo(message.chat.id, photo="https://telegra.ph/file/55e27bacddf487d920a1a.jpg", caption=user_profile)












user_partners = {}



@Celestia.on_message(filters.command("setpartner"))
def set_partner_command(client, message):
    user_id = message.from_user.id
    name = message.from_user.first_name

    reply = message.reply_to_message
    if reply:
        user = reply.from_user
    else:
        message.reply("Please reply to the user you want to set as a partner.")
        return

    if user_id not in user_database:
        message.reply("Please create your character first using the /character command.")
        return

    if user.id not in user_database:
        message.reply("Target user not found in the database.")
        return

    user_family[user_id] = {
        "partner": user.id,
        "son": None,
        "daughter": None,
        "brothers": None,
        "sister": None
    }

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔴 YES", callback_data="confirm_partner"),
         InlineKeyboardButton("🔵 NO", callback_data="cancel_partner")]
    ])
    message.reply_text(f"Congratulations! You are now partners with {user.first_name}.", reply_markup=reply_markup)






@Celestia.on_callback_query(filters.regex("confirm_partner"))
def callback_confirm_partner(client, callback_query):
    user_id = callback_query.from_user.id
    partner_id = user_family[user_id]["partner"]
    
    if partner_id:
        partner_name = user_partners.get(partner_id, "your partner")
        callback_query.answer(f"You've confirmed {partner_name} as your partner!")
    else:
        callback_query.answer("Your partner is not set. Please set a partner first.")
    
    



@Celestia.on_callback_query(filters.regex("cancel_partner"))
def callback_cancel_partner(client, callback_query):
    user_id = callback_query.from_user.id
    user_family[user_id]["partner"] = None
    callback_query.answer("You've canceled your partner selection.")





                            





    



@Celestia.on_message(filters.command("fight", prefixes="/"))
def fight_command(client, message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    
    reply = message.reply_to_message
    if reply:
        target_user = reply.from_user
    else:
        target_user = get_arg(message)
        if not target_user:
            client.send_message(message.chat.id, "**Whom should I fight?**")
            return

    if user_id not in user_database:
        client.send_message(message.chat.id, "Please create your character first using the /character command.")
        return

    if target_user.id not in user_database:
        client.send_message(message.chat.id, "Target user not found in the database.")
        return

    initiating_user_health = user_database[user_id]["health"]
    target_user_health = user_database[target_user.id]["health"]

    damage_initiator = random.randint(10, 30)
    damage_target = random.randint(10, 30)

    initiating_user_health -= damage_target
    target_user_health -= damage_initiator

    winner = user_id if initiating_user_health > target_user_health else target_user.id

    result_message = f"{name} dealt {damage_initiator} damage. {target_user.first_name} dealt {damage_target} damage.\n"
    result_message += f"{name} has {initiating_user_health} health. {target_user.first_name} has {target_user_health} health.\n"
    result_message += f"The winner is {winner}!"

    client.send_message(message.chat.id, result_message)




