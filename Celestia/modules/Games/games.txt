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
character_collection = db["characters"]
users_collection = db["game_users"]


DICT = {}

    
    
# =================> ADD- QUIZ <================= #

@Celestia.on_message(filters.command("addquiz") & filters.user(SUDO_USERS))
async def add_quiz(_, message):
    if len(message.text) < 11:
        return await message.reply("**Please provide the quiz details in the format:**\n\n /addquiz quiz_url+question+option1+option2+option3+option4+correct_answer**")
    if not message.text.split(maxsplit=1)[1]:
        return await message.reply("**Please provide the quiz details in the format:**\n\n /addquiz quiz_url+question+option1+option2+option3+option4+correct_answer**")
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
    await _.send_message(-1001946875647, text=f"**ǫᴜɪᴢ ǫᴜᴇsᴛɪᴏɴ ᴜᴘʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴇᴄᴋ ᴏɴ ǫᴜɪᴢ ɢᴀᴍᴇs**[🎉]({quiz_url})", reply_markup=InlineKeyboardMarkup([[
     InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
      ]]))
    await message.reply("**🎉 ǫᴜɪᴢ ǫᴜᴇsᴛɪᴏɴs sᴜᴄᴄᴇssғᴜʟʟʏ sᴀᴠᴇᴅ ɪɴ ʏᴏᴜʀ ǫᴜɪᴢ ᴅᴀᴛᴀʙᴀsᴇ !**")


# =================> sʜᴏᴘ-ᴄʜᴀʀᴀᴄᴛᴇʀs <================= #

@Celestia.on_message(filters.command("addchar") & filters.user(SUDO_USERS))
async def add_char(_, message):
    if len(message.text) < 11:
        return await message.reply("**Please provide the character shops details in the format:**\n\n /addchar img_url+name+level+price**")
    if not message.text.split(maxsplit=1)[1]:
        return await message.reply("**Please provide the character shops details in the format:**\n\n /addchar img_url+name+level+price**")
    char_details = message.text.split(maxsplit=1)[1]
    data = char_details.split("+")
    if not data[0].startswith("https"):
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ɪᴍɢ ʟɪɴᴋ.**")
    if not data[1]:
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ᴄʜᴀʀᴀᴄᴛᴇʀ ɴᴀᴍᴇ.**")
    if not data[3]:
        return await message.reply("**sᴡᴇᴇᴛʜᴇᴀʀᴛ ɪ ᴛʜɪɴᴋ ʏᴏᴜ ғᴏʀɢᴇᴛ ᴄᴏʀʀᴇᴄᴛ ᴘʀɪᴄᴇ.**")
    
    img_url, name, level, price = data
    
    img_url = img_url
    name = name.title()
    level = int(level)
    price = int(price)
    
    
    char_data = {
        "img_url": img_url,
        "name": name,
        "level": level,
        "price": price
    }
    latest_char = questions_collection.find_one(sort=[("_id", -1)])
    object_id = latest_char.get("_id")

    
    character_collection.insert_one(char_data)
    await _.send_photo(-1002090470079, photo=img_url, caption=f"**📝 ɴᴀᴍᴇ**: {name}\n\n**📈 ʟᴇᴠᴇʟ**: {level}\n**💰 ᴘʀɪᴄᴇ**: ${price} Shells\n**📊 ɪᴅ**: `{object_id}`", reply_markup=InlineKeyboardMarkup([[
     InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
      ]]))
    await _.send_message(-1001946875647, text=f"**sʜᴏᴘs ᴀssᴇᴛs ᴜᴘʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴇᴄᴋ ᴏɴ sʜᴏᴘs**[🎉]({img_url})", reply_markup=InlineKeyboardMarkup([[
     InlineKeyboardButton(f"{message.from_user.first_name}", url=f"https://t.me/{message.from_user.username}"),    
      ]]))
    await message.reply("**🎉 sʜᴏᴘs ᴀssᴇᴛs sᴜᴄᴄᴇssғᴜʟʟʏ sᴀᴠᴇᴅ ɪɴ ʏᴏᴜʀ sʜᴏᴘs ᴅᴀᴛᴀʙᴀsᴇ !**")



# =================> ǫᴜɪᴢ-ᴡᴀᴄᴛᴄʜᴇʀ <================= #

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

    
# =================> ᴅᴇʟ-ᴅᴀᴛᴀʙᴀsᴇs <================= #

@Celestia.on_message(filters.command("deldb") & filters.user(SUDO_USERS))
async def delete_quizes(_, message):
    try:
        query = message.text.split(None, 1)[1]
        msg = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
        result = questions_collection.delete_one({"_id": ObjectId(query)})

        if result.deleted_count == 1:
            await msg.edit("**ᴏʙᴊᴇᴄᴛ ɪᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ.**")
        else:
            await msg.edit("**ᴏʙᴊᴇᴄᴛ ᴅᴏᴇs ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ !!**")
    except Exception as e:
        await msg.edit(f"**ᴇʀʀᴏʀ**: {str(e)}")


@Celestia.on_message(filters.command("delchar") & filters.user(SUDO_USERS))
async def delete_character(_, message):
    try:
        query = message.text.split(None, 1)[1]
        msg = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
        result = character_collection.delete_one({"_id": ObjectId(query)})

        if result.deleted_count == 1:
            await msg.edit("**ᴏʙᴊᴇᴄᴛ ɪᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ.**")
        else:
            await msg.edit("**ᴏʙᴊᴇᴄᴛ ᴅᴏᴇs ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ !!**")
    except Exception as e:
        await msg.edit(f"**ᴇʀʀᴏʀ**: {str(e)}")


# =================> ǫᴜɪᴢ-ᴀɴsᴡᴇʀ <================= #

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
            await query.answer("ʏᴏᴜʀ ᴀɴsᴡᴇʀ ɪs ᴄᴏʀʀᴇᴄᴛ !!")

            await create_account(user_id,query.from_user.username)
            coins = await user_wallet(user_id)     
            await gamesdb.update_one({'user_id' : user_id},{'$set' : {'coins' : coins + 300}},upsert=True)
            await query.edit_message_text(f"🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs {query.from_user.mention}! ʏᴏᴜʀ ɢᴜᴇss ɪs sᴘᴏᴛ ᴏɴ, ᴀɴᴅ ʏᴏᴜ'ᴠᴇ ᴡᴏɴ 300 sʜᴇʟʟs. ᴡᴇʟʟ ᴅᴏɴᴇ!\nᴄᴜʀʀᴇɴᴛ ʙᴀʟᴀɴᴄᴇ ✑  `{0:,}` sʜᴇʟʟs".format(coins+300))    
                              
        else:
            await query.answer("ʏᴏᴜʀ ᴀɴsᴡᴇʀ ɪs ᴡʀᴏɴɢ !!")
            await query.edit_message_text(f"ᴜɴғᴏʀᴛᴜɴᴀᴛᴇʟʏ {query.from_user.mention}!, ʏᴏᴜʀ ɢᴜᴇss ᴡᴀsɴ'ᴛ ᴀᴄᴄᴜʀᴀᴛᴇ ᴛʜɪs ᴛɪᴍᴇ, sᴏ ʏᴏᴜ ᴡᴏɴ'ᴛ ʙᴇ ᴀᴡᴀʀᴅᴇᴅ ᴀɴʏ sʜᴇʟʟs so ʏᴏᴜ ᴡᴏɴ'ᴛ ʙᴇ ᴀᴡᴀʀᴅᴇᴅ ᴀɴʏ sʜᴇʟʟs. ᴋᴇᴇᴘ ᴛʀʏɪɴɢ, ᴀɴᴅ ʙᴇᴛᴛᴇʀ ʟᴜᴄᴋ ɴᴇxᴛ ᴛɪᴍᴇ !")




# =================> ǫᴜɪᴢ-ᴄʜᴀʀᴀᴄᴛᴇʀs <================= #


result = questions_collection.find()
quizzes = list(result)
current_index = 0


@Celestia.on_message(filters.command("quizes"))
async def show_photo(_, message):
    
    photo = quizzes[current_index]["quiz_url"]

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴘʀᴇᴠ", callback_data="back"),
                InlineKeyboardButton("ɴᴇxᴛ", callback_data="next")                
            ]
        ]
    )

    await message.reply_photo(photo=photo, reply_markup=keyboard)
    


# =================> ɢᴀᴍᴇ-sʜᴏᴘs <================= #

@Celestia.on_message(filters.command("shop"))
async def shops(_, message):
    buttons = InlineKeyboardMarkup(
        [[
                InlineKeyboardButton("ᴄʜᴀʀᴀᴄᴛᴇʀ", callback_data="char_"),
                InlineKeyboardButton("ᴍᴀɢɪᴄ", callback_data="maintainer_")                
        ]]
    )
    await message.reply_photo(photo="https://telegra.ph/file/e325e6a24e9a2227ef3d2.jpg", caption="ᴛᴇxᴛ", reply_markup=buttons)



@Celestia.on_message(filters.command("explore"))
async def explore_command(_, message):
    result = questions_collection.find()
    lol = list(result)
    data = random.choice(lol)
    photo = data["quiz_url"]

    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("let's fight", callback_data="maintainer_"),
                InlineKeyboardButton("info", callback_data="maintainer_")
            ]
        ]
    )

    await message.reply_photo(photo, caption="You wanna fight with me bwhahaha", reply_markup=button)



# =================> sʜᴏᴘ-ᴄʜᴀʀᴀᴄᴛᴇʀs <================= #

result = character_collection.find()
char = list(result)
char_index = 0



@Celestia.on_callback_query(filters.regex("^char_$"))
async def char_photo(_, query):
    global char_index

    photo = char[char_index]["img_url"]
    name = char[char_index]["name"]
    level = char[char_index]["level"]
    price = char[char_index]["price"]

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴘʀᴇᴠ", callback_data="backc"),
                InlineKeyboardButton("ɴᴇxᴛ", callback_data="nextc")
            ]
        ]
    )

    user_id = query.from_user.id
    reply = query.message.reply_to_message
    sexi_id = reply.from_user.id

    if user_id == sexi_id:
        await query.message.edit_media(
            media=InputMediaPhoto(photo,
            caption=f"**📝 ɴᴀᴍᴇ**: {name}\n\n**📈 ʟᴇᴠᴇʟ**: {level}\n**📊 ᴘʀɪᴄᴇ**: ${price} Shells"),
            reply_markup=keyboard
        )
    else:
        await query.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ !!")




@Celestia.on_callback_query(filters.regex("^nextc$"))
async def next_char(_, query):
    global char_index
    if char_index < len(char) - 1:
        char_index += 1
    photo = char[char_index]["img_url"]
    name = char[char_index]["name"]
    level = char[char_index]["level"]
    price = char[char_index]["price"]
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴘʀᴇᴠ", callback_data="backc"),
                InlineKeyboardButton("ɴᴇxᴛ", callback_data="nextc")
            ]
        ]
    )
    user_id = query.from_user.id
    reply = query.message.reply_to_message
    sexi_id = reply.from_user.id

    if user_id == sexi_id:
        await query.message.edit_media(
            media=InputMediaPhoto(photo,
            caption=f"**📝 ɴᴀᴍᴇ**: {name}\n\n**📈 ʟᴇᴠᴇʟ**: {level}\n**📊 ᴘʀɪᴄᴇ**: ${price} Shells"),
            reply_markup=keyboard
        )
    else:
        await query.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ !!")



@Celestia.on_callback_query(filters.regex("^backc$"))
async def back_char(_, query):
    global char_index
    if char_index > 0:
        char_index -= 1

    photo = char[char_index]["img_url"]
    name = char[char_index]["name"]
    level = char[char_index]["level"]
    price = char[char_index]["price"]
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴘʀᴇᴠ", callback_data="backc"),
                InlineKeyboardButton("ɴᴇxᴛ", callback_data="nextc")
            ]
        ]
    )
    user_id = query.from_user.id
    reply = query.message.reply_to_message
    sexi_id = reply.from_user.id

    if user_id == sexi_id:
        await query.message.edit_media(
            media=InputMediaPhoto(photo,
            caption=f"**📝 ɴᴀᴍᴇ**: {name}\n\n**📈 ʟᴇᴠᴇʟ**: {level}\n**📊 ᴘʀɪᴄᴇ**: ${price} Shells"),
            reply_markup=keyboard
        )
    else:
        await query.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ !!")



# =================> ǫᴜɪᴢ-ᴄʜᴀʀᴀᴄᴛᴇʀs <================= #

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
                InlineKeyboardButton("ᴘʀᴇᴠ", callback_data="back"),
                InlineKeyboardButton("ɴᴇxᴛ", callback_data="next")         
            ]
        ]
    )
    if user_id == sexi_id:
        await query.message.edit_media(
         media=InputMediaPhoto(photo),
         reply_markup=keyboard
       )
    else:
        await query.answer("ʀʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ !!")



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
                InlineKeyboardButton("ᴘʀᴇᴠ", callback_data="back"),
                InlineKeyboardButton("ɴᴇxᴛ", callback_data="next")                
            ]
        ]
    )

    if user_id == sexi_id:
        await query.message.edit_media(
         media=InputMediaPhoto(photo),
         reply_markup=keyboard
      )

    else:
        await query.answer("ᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ !!")









