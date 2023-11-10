import asyncio
from bson import ObjectId
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import pymongo, re, random
from config import MONGO_URL, SUDO_USERS
from Celestia import Celestia
from Celestia.modules.games import *



client = pymongo.MongoClient(MONGO_URL)
db = client["quiz_games"]
questions_collection = db["questions"]
shops_collection = db["shops"]


DICT = {}

    
    
# =================> ADD- QUIZ <================= #

@Celestia.on_message(filters.command("addquiz") & filters.user(SUDO_USERS))
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
    
    quiz_url = quiz_url
    question = question.title()
    option1 = option1.title()
    option2 = option2.title()
    option3 = option3.title()
    option4 = option4.title()
    correct_answer = correct_answer.title()
    
    
    quiz_data = {
        "quiz_url": quiz_url,
        "question": question,
        "options": [option1, option2, option3, option4],
        "correct_answer": correct_answer
    }
    latest_quiz = questions_collection.find_one(sort=[("_id", -1)])
    object_id = latest_quiz.get("_id")

    
    questions_collection.insert_one(quiz_data)
    await _.send_photo(-1002066177399, photo=quiz_url, caption=f"**📰 ǫᴜᴇsᴛɪᴏɴ**: {question}\n\n**📝 ᴀɴsᴡᴇʀᴇ**: {correct_answer}\n**📊 ɪᴅ**: `{object_id}`", reply_markup=InlineKeyboardMarkup([[
     InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
      ]]))
    await _.send_message(-1001946875647, text=f"**ǫᴜɪᴢ ǫᴜᴇsᴛɪᴏɴ ᴜᴘʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴇᴄᴋ ᴏɴ ǫᴜɪᴢ ɢᴀᴍᴇs**[🎉]({data[0]})", reply_markup=InlineKeyboardMarkup([[
     InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
      ]]))
    await message.reply("**🎉 ǫᴜɪᴢ ǫᴜᴇsᴛɪᴏɴs sᴜᴄᴄᴇssғᴜʟʟʏ sᴀᴠᴇᴅ ɪɴ ʏᴏᴜʀ ǫᴜɪᴢ ᴅᴀᴛᴀʙᴀsᴇ !**")


# =================> ADD - SHOP <================= #


@Celestia.on_message(filters.command("addchar") & filters.user(SUDO_USERS))
async def shop_char(_, message):
    if len(message.text) < 5:
        return await message.reply("**Please provide the character details in the format:**\n\n /addchar img_url+name+level+price")
    
    char_details = message.text.split(maxsplit=1)[1]
    data = char_details.split("+")
    
    if len(data) != 4:
        return await message.reply("**Invalid format. Please check the character details format.**")

    img_url, name, level, price = data
    
    if not img_url.startswith("https"):
        return await message.reply("**Invalid image URL. Please provide a valid URL.**")
    if not name:
        return await message.reply("**Please provide the character name.**")
    if not level:
        return await message.reply("**Please provide the character level.**")
    if not price:
        return await message.reply("**Please provide the character price.**")

    name = name.title()
    level = level.title()

    char_data = {
        "img_url": img_url,
        "name": name,
        "level": level,
        "price": price
    }

    
    latest_char = questions_collection.find_one(sort=[("_id", -1)])
    object_id = latest_char.get("_id", 0) + 1


    char_data_id = f"{object_id:02d}"
    shops_collection.insert_one({char_data_id: char_data})


    await _.send_photo(-1002090470079, photo=img_url, caption=f"**📝 Name:** {name}\n\n**📈 Level:** {level}\n**📊 Price:** {price}", reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
    ]]))
    
    await _.send_message(-1001946875647, text=f"**Character added successfully!**\n\n**ID:** {char_data_id}\n**Name:** {name}\n**Level:** {level}\n**Price:** {price}\n\n[View in Shops]({img_url})", reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
    ]]))
    
    await message.reply("🎉 Character data successfully saved in the database with ID: **" + char_data_id + "**")





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

    



        
@Celestia.on_message(filters.command("deldb") & filters.user(SUDO_USERS))
async def delete_document(_, message):
    try:
        query = message.text.split(None, 1)[1]
        msg = await message.reply("processing...")
        result = questions_collection.delete_one({"_id": ObjectId(query)})

        if result.deleted_count == 1:
            await msg.edit("**ᴏʙᴊᴇᴄᴛ ɪᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ.**")
        else:
            await msg.edit("**ᴏʙᴊᴇᴄᴛ ᴅᴏᴇs ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ !!**")
    except Exception as e:
        await msg.edit(f"**ᴇʀʀᴏʀ**: {str(e)}")


@Celestia.on_callback_query(filters.regex(r'^answer_\w+'))
async def callback_answer(client, query):
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    user_answer = query.data.replace('answer_', '')

    if chat_id in DICT and DICT[chat_id].get("correct_answer"):
        correct_answer = DICT[chat_id]['correct_answer']
        print(user_answer)

        if user_answer == correct_answer:
            DICT.pop(chat_id)
            await query.answer("your answer is correct!!")

            await create_account(user_id,query.from_user.username)
            coins = await user_wallet(user_id)     
            await gamesdb.update_one({'user_id' : user_id},{'$set' : {'coins' : coins + 300}},upsert=True)
            await query.edit_message_text("Congratulations! Your guess is spot on, and you've won 300 shells. Well done!\nCurrent Balance ✑  `{0:,}` Shell".format(coins+300))    
                              
        else:
            await query.answer("your answer is wrong!!")
            await query.edit_message_text(f"Unfortunately, your guess wasn't accurate this time, so you won't be awarded any shells. Keep trying, and better luck next time!")



result = questions_collection.find()
quizzes = list(result)
current_index = 0


@Celestia.on_message(filters.command("quizes"))
async def show_photo(_, message):
    
    photo = quizzes[current_index]["quiz_url"]

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back", callback_data="back"),
                InlineKeyboardButton("Next", callback_data="next")                
            ]
        ]
    )

    await message.reply_photo(photo=photo, reply_markup=keyboard)
    



@Celestia.on_callback_query(filters.regex("^next$"))
async def next_photo(_, query):
    user_id = query.from_user.id
    reply = query.message.reply_to_message
    sexi_id = reply.from_user.id
    global current_index
    if current_index < len(quizzes) - 1:
        current_index += 1
    photo = quizzes[current_index]["quiz_url"]
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back", callback_data="back"),
                InlineKeyboardButton("Next", callback_data="next")         
            ]
        ]
    )
    if user_id == sexi_id:
        await query.message.edit_media(
         media=InputMediaPhoto(photo),
         reply_markup=keyboard
       )
    else:
        await query.answer("This is not for you !!")



@Celestia.on_callback_query(filters.regex("^back$"))
async def back_photo(_, query):
    user_id = query.from_user.id
    reply = query.message.reply_to_message
    sexi_id = reply.from_user.id
    global current_index
    if current_index > 0:
        current_index -= 1
    
    photo = quizzes[current_index]["quiz_url"]
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back", callback_data="back"),
                InlineKeyboardButton("Next", callback_data="next")                
            ]
        ]
    )

    if user_id == sexi_id:
        await query.message.edit_media(
         media=InputMediaPhoto(photo),
         reply_markup=keyboard
      )

    else:
        await query.answer("This is not for you !!")


    
        
