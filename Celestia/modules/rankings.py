from pyrogram import filters
from pymongo import MongoClient, DESCENDING
from config import MONGO_URL
from Celestia import Celestia as Client

client = MongoClient(MONGO_URL)
db = client['message_counts']
collection = db['group_message_counts']

@Client.on_message(filters.group)
async def track_message_count(client, message):
    # Check if the message is from a group
    user_id = message.from_user.id

    # Check if the user is already in the database
    user_data = collection.find_one({'user_id': user_id})
    if user_data:
        collection.update_one({'user_id': user_id}, {'$inc': {'message_count': 1}})
    else:
        collection.insert_one({'user_id': user_id, 'message_count': 1})

@Client.on_message(filters.command('rank', prefixes='/'))
async def top_message_senders(client, message):
    # Get the top 10 users with the highest message counts
    top_users = collection.find().sort('message_count', DESCENDING).limit(10)
    
    response = "Top 10 message senders:\n"
    for index, user_data in enumerate(top_users, 1):
        user_id = user_data['user_id']
        user = await client.get_users(user_id)  # Corrected 'app' to 'client'
        response += f"{index}. {user.first_name} {user.last_name} ({user.username}): {user_data['message_count']} messages\n"
    
    await message.reply(response)



      
