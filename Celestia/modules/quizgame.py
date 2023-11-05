import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pymongo, re, random
from config import MONGO_URL, OWNER_ID
from Celestia import Celestia


client = pymongo.MongoClient(MONGO_URL)
db = client["quiz_games_db"]
questions_collection = db["questions"]
winners_collection = db["winners"]


DICT = {}




def get_top_10_winners():
    top_winners = winners_collection.aggregate([
        {"$group": {"_id": "$user_id", "username": {"$first": "$username"}, "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    return [winner["username"] for winner in top_winners]









@Celestia.on_message(filters.command("addquiz") & filters.user(OWNER_ID))
async def add_quiz(_, message):
    if len(message.text) < 11:
        return await message.reply("**Please provide the quiz details in the format:**\n\n /addquiz quiz_url+question+option1+option2+option3+option4+correct_answer")
    if not message.text.split(maxsplit=1)[1]:
        return await message.reply("**Please provide the quiz details in the format:**\n\n /addquiz quiz_url+question+option1+option2+option3+option4+correct_answer")
    quiz_details = message.text.split(maxsplit=1)[1]
    data = quiz_details.split("+")
    if not data[0].startswith("https"):
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ǫᴜɪᴢ ʟɪɴᴋ.**")
    if not data[1]:
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ǫᴜɪᴢ ǫᴜᴇsᴛɪᴏɴ.**")
    if not data[2:5]:
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ᴏᴘᴛɪᴏɴs.**")
    if not data[6]:
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ correct answere.**")
    
  
    quiz_url, question, option1, option2, option3, option4, correct_answer = data
    quiz_data = {
        "quiz_url": quiz_url,
        "question": question,
        "options": [option1, option2, option3, option4],
        "correct_answer": correct_answer
    }
    
    questions_collection.insert_one(quiz_data)
    await message.reply("Quiz added successfully!")



# =================> wacther <=================== #












@Celestia.on_message(filters.group, group=11)
async def _watcher(client, message):
    chat_id = message.chat.id
    if not message.from_user:
        return

    if chat_id not in DICT:
        DICT[chat_id] = {'count': 0, 'running_count': 0, 'quiz_url': None, 'question': None, 'options': None, 'correct_answer': None}
    
    DICT[chat_id]['count'] += 1

    if DICT[chat_id]['count'] == 10:
        result = questions_collection.find()
        quizes = list(result)
        data = random.choice(quizes)
        photo = data["quiz_url"]
        question = data["question"]
        options = data["options"]
        correct = data["correct_answer"]
        try:
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(option, callback_data=f"answer_{option}")]
                for option in options
            ])

            await client.send_photo(
                chat_id,
                photo=photo,
                caption=f"Question: {question}",
                reply_markup=keyboard
            )
            DICT[chat_id]["quiz_url"] = photo
            DICT[chat_id]["question"] = question
            DICT[chat_id]["options"] = options
            DICT[chat_id]["correct_answer"] = correct
        except errors.FloodWait as e:
            await asyncio.sleep(e.x)
    
    if DICT[chat_id].get('correct_answer'):
        DICT[chat_id]['running_count'] += 1
        if DICT[chat_id]['running_count'] == 30:
            try:
                correct_answer = DICT[chat_id]['correct_answer']
                await client.send_message(chat_id, f"**correct answer is **: {correct_answer}\n**Make sure to remember it next time.**")
                DICT.pop(chat_id)
            except errors.FloodWait as e:
                await asyncio.sleep(e.x)






@Celestia.on_callback_query(filters.regex(r'^answer_\w+'))  # Regex filter for callback data
async def callback_answer(client, callback_query):
    chat_id = callback_query.message.chat.id
    if DICT.get(chat_id) and not DICT[chat_id]["answered"]:
        DICT[chat_id]["answered"] = True
        correct_answer = DICT[chat_id]['correct_answer']
        user_answer = callback_query.data.replace('answer_', '')  # Extract the user's answer
        if user_answer == correct_answer:
            await callback_query.answer(f"**Your answer is correct!**")
        else:
            await callback_query.answer(f"**Your answer is wrong!")




@Celestia.on_message(filters.command("ranks"))
async def display_top_10_winners(client, message):
    top_winners = get_top_10_winners()
    if top_winners:
        winners_text = "\n".join([f"{i+1}. {username}" for i, username in enumerate(top_winners)])
        await message.reply(f"Top 10 Winners:\n{winners_text}")
    else:
        await message.reply("No winners yet!")









