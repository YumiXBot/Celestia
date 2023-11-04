from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pymongo, re
from config import MONGO_URL
from Celestia import Celestia


client = pymongo.MongoClient(MONGO_URL)
db = client["quiz_games_db"]
questions_collection = db["questions"]
winners_collection = db["winners"]





def create_quiz_keyboard_regex(question):
    options = question["options"]
    buttons = [InlineKeyboardButton(f"Option {i+1}", callback_data=f"option_{i+1}") for i in range(4)]
    keyboard = InlineKeyboardMarkup([buttons])
    return keyboard



def get_top_10_winners():
    top_winners = winners_collection.aggregate([
        {"$group": {"_id": "$user_id", "username": {"$first": "$username"}, "count": {"$sum": 1}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    return [winner["username"] for winner in top_winners]







@Celestia.on_message(filters.command("addquiz") & filters.user(SUDO_USERS))
async def add_quiz(_, message):
    if len(message.text) < 7:
        return await message.reply("**Please provide the quiz details in the format:** /addquiz quiz_url+question+option1+option2+option3+option4+correct_answer")
    if not message.text.split(maxsplit=1)[1]:
        return await message.reply("**Please provide the quiz details in the format:** /addquiz quiz_url+question+option1+option2+option3+option4+correct_answer")
    quiz_details = message.text.split(maxsplit=1)[1]
    data = quiz_details.split("+")
    if not data[0].startswith("https"):
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ᴡᴀɪғᴜ ʟɪɴᴋ.**")
    if not data[1]:
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ᴡᴀɪғᴜ ɴᴀᴍᴇ.**")
    if not data[2]:
        return await message.reply_text("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ᴀɴɪᴍᴇ ɴᴀᴍᴇ.**")
    if not data[3]:
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ᴡᴀɪғᴜ ʀᴀʀɪᴛʏ.**")
    
  
    question, option1, option2, option3, option4, correct_answer = data
    quiz_data = {
        "quiz_url": quiz_url
        "question": question,
        "options": [option1, option2, option3, option4],
        "correct_answer": int(correct_answer)
    }
    
    questions_collection.insert_one(quiz_data)
    await message.reply("Quiz added successfully!")





"""


option_pattern = re.compile(r'^option_([1-4])$')

@Celestia.on_callback_query(option_pattern)
async def check_answer_regex(client, callback_query):
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username
    selected_option = int(callback_query.matches[0].group(1))
    question = get_question_by_id(callback_query.message.message_id)
    if question and selected_option == question["correct_answer"]:
        winners_collection.insert_one({"user_id": user_id, "username": username, "question_id": question["_id"]})
        await callback_query.answer("Correct answer! You are a winner.")
    else:
        await callback_query.answer("Wrong answer. Try again next time.")



@app.on_message(filters.command("ranks"))
async def display_top_10_winners(client, message):
    top_winners = get_top_10_winners()
    if top_winners:
        winners_text = "\n".join([f"{i+1}. {username}" for i, username in enumerate(top_winners)])
        await message.reply(f"Top 10 Winners:\n{winners_text}")
    else:
        await message.reply("No winners yet!")




"""






