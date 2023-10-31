from pyrogram import Client, filters
import random
from Celestia import Celestia

user_database = {}
user_state = {}

photo = "https://telegra.ph/file/ce3f8731e74c6a75a8321.jpg"

@Celestia.on_message(filters.command("character"))
def character_creation(client, message):
    user_id = message.from_user.id

    if user_id in user_database:
        client.send_message(message.chat.id, "You have already chosen a character.")
        return

    character_name = " ".join(message.command[1:])
    if character_name:
        user_database[user_id] = {"Name": character_name, "health": 100}
        user_state[user_id] = "character_created"
        client.send_message(message.chat.id, f"Character {character_name} created! You can now use the /fight command.")

@Celestia.on_message(filters.command("fight", prefixes="/"))
def fight_command(client, message):
    user_id = message.from_user.id

    if user_id not in user_database:
        client.send_message(message.chat.id, "Please create your character first using the /character command.")
        return

    target_user_id = None
    try:
        target_user_id = int(message.command[1])
    except (IndexError, ValueError):
        client.send_message(message.chat.id, "Please specify a valid target user using `/fight user_id`.")
        return

    if target_user_id not in user_database:
        client.send_message(message.chat.id, "Target user not found in the database.")
        return

    initiating_user_health = user_database[user_id]["health"]
    target_user_health = user_database[target_user_id]["health"]

    damage_initiator = random.randint(10, 30)
    damage_target = random.randint(10, 30)

    initiating_user_health -= damage_target
    target_user_health -= damage_initiator

    winner = user_id if initiating_user_health > target_user_health else target_user_id

    result_message = f"{user_id} dealt {damage_initiator} damage. {target_user_id} dealt {damage_target} damage.\n"
    result_message += f"{user_id} has {initiating_user_health} health. {target_user_id} has {target_user_health} health.\n"
    result_message += f"The winner is {winner}!"

    client.send_message(message.chat.id, result_message)




