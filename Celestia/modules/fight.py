from pyrogram import Client, filters
import random
from Celestia import Celestia

user_database = {}
user_state = {}



def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])




@Celestia.on_message(filters.command("character"))
def character_creation(client, message):
    user_id = message.from_user.id

    if user_id in user_database:
        client.send_message(message.chat.id, "You have already chosen a character.")
        return

    character_name = " ".join(message.command[1:])
    if character_name:
        user_database[user_id] = {"name": character_name, "health": 100, "rank": "Novice Traveler", "partner": None, "family": None, "celeus": 10000}    
        user_state[user_id] = "character_created"
        client.send_photo(message.chat.id, photo="https://telegra.ph/file/55e27bacddf487d920a1a.jpg", caption=f"Character {character_name} created! You can now use the /fight command.")




@Celestia.on_message(filters.command("profile", prefixes="/"))
def profile_command(client, message):
    user_id = message.from_user.id

    if user_id not in user_database:
        client.send_message(message.chat.id, "You haven't created a character yet. Use the /character command to create one.")
        return

    character_data = user_database[user_id]
    profile_message = f"**Character Profile**\n"
    profile_message += f"Name: {character_data['name']}\n"
    profile_message += f"Health: {character_data['health']}\n"
    profile_message += f"Rank: {character_data['rank']}\n"
    profile_message += f"Partner: {character_data['partner']}\n"
    profile_message += f"Family: {character_data['family']}\n"
    profile_message += f"Celeus: {character_data['celeus']}\n"

    client.send_photo(message.chat.id, photo="https://telegra.ph/file/55e27bacddf487d920a1a.jpg", caption=profile_message)









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




