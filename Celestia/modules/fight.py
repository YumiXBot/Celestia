import random
from Celestia import Celestia
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import InputMediaPhoto



def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])




user_database = {}


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
        message.reply("You haven't created a character yet. Use the /character command to create one.")
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
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Family", callback_data="family_profile"),
         InlineKeyboardButton("Shop", callback_data="open_shop")]
    ])

    message.reply_photo(photo="https://telegra.ph/file/55e27bacddf487d920a1a.jpg", caption=user_profile, reply_markup=reply_markup)





user_family = {}

@Celestia.on_message(filters.command("setpartner"))
def set_partner_command(client, message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    reply = message.reply_to_message

    if user_id not in user_database:
        message.reply("Please create your character first using the /character command.")
        return

    if reply:
        user = reply.from_user
        if user.id not in user_database:
            message.reply("Target user not found in the database.")
            return

        # Initialize user_family dictionary for both users
        if user_id not in user_family:
            user_family[user_id] = {
                "partner": None,
                "friends": [],
                "son": [],
                "daughter": [],
                "sister": []
                }
            
        if user.id not in user_family:
            user_family[user.id] = {
                "partner": None,
                "friends": [],
                "son": [],
                "daughter": [],
                "sister": []
                }

        user_family[user_id]["partner"]
        user_family[user.id]["partner"]

        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔴 YES", callback_data="confirm_partner"),
             InlineKeyboardButton("🔵 NO", callback_data="cancel_partner")]
        ])
        message.reply_text(f"Hey {message.from_user.first_name}, would you like to be {user.first_name}'s partner?", reply_markup=reply_markup)

    else:
        message.reply("Please reply to the user you want to set as a partner.")

@Celestia.on_callback_query(filters.regex("confirm_partner"))
async def callback_confirm_partner(client, query):
    user_id = query.from_user.id
    partner_id = user_family.get(user_id).get("partner")

    if partner_id is not None and partner_id == user_id:
        user_family[user_id]["partner"] = partner_id
        user_family[partner_id]["partner"] = user_id

        await query.answer(f"You've confirmed {query.from_user.first_name} as your partner!")
        await query.message.reply("Done!!")
    else:
        await query.answer("Invalid partner selection.")


@Celestia.on_callback_query(filters.regex("cancel_partner"))
async def callback_cancel_partner(client, query):
    user_id = query.from_user.id
    partner_id = user_family.get(user_id, {}).get("partner")

    if partner_id is not None:
        del user_family[user_id]["partner"]
        del user_family[partner_id]["partner"]

        await query.answer(f"You've canceled your partnership with {query.from_user.first_name}.")
        await query.message.reply("Partnership canceled.")

        



@Celestia.on_callback_query(filters.regex("back_profile"))
async def back_profile(client, query):
    user_id = query.from_user.id

    if user_id not in user_database:
        await query.answer("You haven't created a character yet. Use the /character command to create one.")
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
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Family", callback_data="family_profile"),
         InlineKeyboardButton("Shop", callback_data="open_shop")]
    ])

    await query.message.edit_media(
        media=InputMediaPhoto(media="https://telegra.ph/file/55e27bacddf487d920a1a.jpg", caption=user_profile),
        reply_markup=reply_markup
    )






@Celestia.on_callback_query(filters.regex("family_profile"))
async def family_profile(client, query):
    user_id = query.from_user.id

    if user_id not in user_database:
        await query.answer("You haven't created a character yet. Use the /character command to create one.")
        return

    character_data = user_database[user_id]
    character_family = user_family[user_id]
    user_profile = f"""
┏━━━━━━━━━━━━━━━━━
┣ Player family profile 
┗━━━━━━━━━━━━━━━━━

┏━━━━━━━━━⦿
┣⬢ Name : {character_data['name']}
┣⬢ Health : {character_data['health']}
┣⬢ Celeus : {character_data['celeus']}
┗━━━━━━━━━⦿
┏━⦿
┣ Partner : {character_family['partner']}
┣ Friends : {character_family['friends']}
┣ Son : {character_family['son']}
┣ Daughter : {character_family['daughter']}
┣ Sister : {character_family['sister']}
┗━━━━━━━━━⦿
"""
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Back", callback_data="back_profile"),
         InlineKeyboardButton("Shop", callback_data="open_shop")]
    ])

    await query.message.edit_media(
        media=InputMediaPhoto(media="https://graph.org//file/391f2bdd418b41e15b288.jpg", caption=user_profile),
        reply_markup=reply_markup
    )









                

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




