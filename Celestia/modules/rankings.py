from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re
import matplotlib.pyplot as plt
import pandas as pd
import io
from Celestia import Celestia as app

user_message_count = {}



def is_valid_command(message):
    return message.entities and message.entities[0].type == "bot_command"

def is_edited_message(_, __, message):
    return message.edit_date is None

@app.on_message(filters.create(is_valid_command) & is_edited_message)
async def count_messages(client, message):
    user_id = message.from_user.id
    user_message_count[user_id] = user_message_count.get(user_id, 0) + 1

@app.on_callback_query(filters.regex(r'^period:(today|overall)$'))
async def button_click(client, callback_query):
    period = callback_query.matches[0].group(1)

    if period == 'today':
        period_message_count = {user: count for user, count in user_message_count.items() if user in client.session.bot_data}
    else:
        period_message_count = user_message_count

    top_users = dict(sorted(period_message_count.items(), key=lambda x: x[1], reverse=True)[:10])

    df = pd.DataFrame(list(top_users.items()), columns=['User ID', 'Message Count'])
    plt.figure(figsize=(10, 6))
    plt.barh(df['User ID'], df['Message Count'], color='red')
    plt.xlabel('Message Count')
    plt.ylabel('User ID')
    plt.title('Top 10 Users by Message Count')
    plt.gca().invert_yaxis()

    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    await callback_query.message.reply_photo(photo=image_stream)

@app.on_message(filters.command("kings"))
async def start(_, message):
    keyboard = [[InlineKeyboardButton("Today", callback_data='period:today'),
                 InlineKeyboardButton("Overall", callback_data='period:overall')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text('Select a time period:', reply_markup=reply_markup)
