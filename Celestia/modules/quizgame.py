import asyncio
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import pymongo, re, random
from config import MONGO_URL, SUDO_USERS as OWNER_ID
from Celestia import Celestia


client = pymongo.MongoClient(MONGO_URL)
db = client["quiz_games"]
questions_collection = db["questions"]
winners_collection = db["winners"]


DICT = {}




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
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ᴄᴏʀʀᴇᴄᴛ ᴀɴsᴡᴇʀᴇ.**")
    
  
    quiz_url, question, option1, option2, option3, option4, correct_answer = data
    quiz_data = {
        "quiz_url": quiz_url,
        "question": question,
        "options": [option1, option2, option3, option4],
        "correct_answer": correct_answer
    }
    
    questions_collection.insert_one(quiz_data)
    await _.send_photo(-1002066177399, photo=data[0], caption=f"Question: {data[1]}\nAnswere: {data[6]}", reply_markup=InlineKeyboardMarkup([[
     InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
      ]]))
    await _.send_message(-1001946875647, text=f"**ǫᴜɪᴢ ǫᴜᴇsᴛɪᴏɴ ᴜᴘʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴇᴄᴋ ᴏɴ ǫᴜɪᴢ ɢᴀᴍᴇs**[🎉]({data[0]})", reply_markup=InlineKeyboardMarkup([[
     InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
      ]]))
    await message.reply("**🎉 ǫᴜɪᴢ ǫᴜᴇsᴛɪᴏɴs sᴜᴄᴄᴇssғᴜʟʟʏ sᴀᴠᴇᴅ ɪɴ ʏᴏᴜʀ ǫᴜɪᴢ ᴅᴀᴛᴀʙᴀsᴇ !**")






@Celestia.on_message(filters.group, group=11)
async def _watcher(client, message):
    chat_id = message.chat.id
    if not message.from_user:
        return

    if chat_id not in DICT:
        DICT[chat_id] = {'count': 0, 'running_count': 0, 'quiz_url': None, 'question': None, 'options': None, 'correct_answer': None, 'user_answers': None}
    
    DICT[chat_id]['count'] += 1

    if DICT[chat_id]['count'] == 100:
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
                caption=f"**ǫᴜᴇsᴛɪᴏɴ**: {question}",
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
                await client.send_message(chat_id, f"****ᴄᴏʀʀᴇᴄᴛ ᴀɴsᴡᴇʀ ɪs **: {correct_answer}\n**ᴍᴀᴋᴇ sᴜʀᴇ ᴛᴏ ʀᴇᴍᴇᴍʙᴇʀ ɪᴛ ɴᴇxᴛ ᴛɪᴍᴇ.**")
                DICT.pop(chat_id)
            except errors.FloodWait as e:
                await asyncio.sleep(e.x)

    



@Celestia.on_callback_query(filters.regex(r'^answer_\w+'))
async def callback_answer(client, query):
    chat_id = query.message.chat.id
    user_answer = query.data.replace('answer_', '')

    if chat_id in DICT and DICT[chat_id].get("correct_answer"):
        correct_answer = DICT[chat_id]['correct_answer']
        print(user_answer)

        if user_answer == correct_answer:
            DICT.pop(chat_id)
            await query.edit_message_text(f"{query.from_user.mention} **Your answer is correct!**")
        else:
            await query.edit_message_text(f"{query.from_user.mention} **Your answer is wrong!**")

        
        






photos = []  

current_photo_index = 0


def send_current_photo(chat_id):
    result = questions_collection.find()
    data = list(result)
    photo = data[current_photo_index]["quiz_url"]
    with open(photos[current_photo_index], 'rb') as photo_file:
        # Replace Celestia.send_photo with the appropriate method for sending photos
        client.send_photo(chat_id, photo=photo_file, caption=f'Photo {current_photo_index + 1}/{len(photos)}', reply_markup=get_keyboard())


def get_keyboard():
    buttons = [
        InlineKeyboardButton("Previous", callback_data="photo_prev"),
        InlineKeyboardButton("Next", callback_data="photo_next"),
    ]
    return InlineKeyboardMarkup([buttons])


@Celestia.on_message(filters.command("xtest"))
def send_photo_command(client, message):
    global current_photo_index
    chat_id = message.chat.id
    current_photo_index = 0
    send_current_photo(chat_id)


photo_callback_pattern = re.compile(r'^photo_(prev|next)$')

@Celestia.on_callback_query(photo_callback_pattern)
def regex_button_click(client, query):
    global current_photo_index
    chat_id = query.message.chat.id
    data = query.data

    match = photo_callback_pattern.match(data)
    if match:
        button_action = match.group(1)
        if button_action == 'prev':
            current_photo_index = (current_photo_index - 1) % len(photos)
        elif button_action == 'next':
            current_photo_index = (current_photo_index + 1) % len(photos)

        send_current_photo(chat_id)
        query.answer()


