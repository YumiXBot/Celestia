import random, re
from bson import ObjectId
from Celestia import Celestia
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Celestia.modules.quizgame import users_collection
from pyrogram.types import InputMediaPhoto
from config import SUDO_USERS



disc1 = """
ɴᴇꜰᴇʀᴛᴀʀɪ ᴅ. ᴠɪᴠɪ :  ꜱʜᴇ ɪꜱ ᴛʜᴇ ᴘʀɪɴᴄᴇꜱꜱ ᴏꜰ ᴀʟᴀʙᴀꜱᴛᴀ ᴋɪɴɢᴅᴏᴍ. ꜱʜᴇ ᴏɴᴄᴇ ᴡᴏʀᴋᴇᴅ ᴀꜱ ᴀ ᴜɴᴅᴇʀᴄᴏᴠᴇʀᴇᴅ ᴀɢᴇɴᴛ ɪɴ ʙᴀʀᴏQᴜᴇ ᴡᴏʀᴋꜱ.ᴠɪᴠɪ ᴀʟʟɪᴇᴅ ᴡɪᴛʜ ᴛʜᴇ ꜱᴛʀᴀᴡʜᴀᴛꜱ. ꜱʜᴇ ᴀʟᴏɴɢ ꜱᴀɪʟᴇᴅ ᴡɪᴛʜ ᴛʜᴇᴍ ᴛᴏ ᴀʟᴀʙᴀꜱᴛᴀ ᴀɴᴅ ᴛᴏ ᴛᴀᴋᴇ ᴅᴏᴡɴ ᴄʀᴏᴄᴏᴅɪʟᴇ. ᴛʜᴇʀᴇ ʜᴀᴘᴘᴇɴᴇᴅ ᴀ ᴡᴀʀ ᴀɢᴀɪɴꜱᴛ ᴛʜᴇ ᴄɪᴛɪᴢᴇɴꜱ ᴀɴᴅ ᴛʜᴇ ᴍᴇᴍʙᴇʀꜱ ᴏꜰ ʙᴀʀᴏQᴜᴇ ᴡᴏʀᴋꜱ. ɪɴ ᴛʜᴇ ʟᴀꜱᴛ ʟᴜꜰꜰʏ ᴛᴏᴏᴋ ᴅᴏᴡɴ ᴄʀᴏᴄᴏᴅɪʟᴇ ᴀɴᴅ ᴄʀᴏᴄᴏᴅɪʟᴇ ᴡᴀꜱ ꜱᴇɴᴅ ᴛᴏ ᴛʜᴇ ɪᴍᴘᴇʟ ᴅᴏᴡɴ ᴀꜱ ᴀ ᴘʀɪꜱᴏɴᴇʀ. ᴠɪᴠɪ ʙᴇᴄᴀᴍᴇ ᴛʜᴇ ᴘʀɪɴᴄᴇꜱꜱ ᴏɴᴄᴇ ᴀɢᴀɪɴ
"""

disc2 = """
ꜱʜɪᴋᴀᴍᴀʀᴜ ɴᴀʀᴀ :  ꜱʜɪᴋᴀᴍᴀʀᴜ ɪꜱ ᴀ ꜱʜɪɴᴏʙɪ ꜰʀᴏᴍ ᴛʜᴇ ɴᴀʀᴀ ᴄʟᴀɴ. ʜᴇ ɪꜱ ʟᴀᴢʏ ʙʏ ʜɪꜱ ɴᴀᴛᴜʀᴇ ʙᴜᴛ ʜᴇ ɪꜱ ᴠᴇʀʏ ɪɴᴛᴇʟʟɪɢᴇɴᴛ. ʜᴇ ᴡᴀꜱ ᴀ ᴍᴇᴍʙᴇʀ ᴏꜰ ᴛʜᴇ ᴛᴇᴀᴍ ᴀꜱᴜᴍᴀ ᴀᴋᴀ ᴛᴇᴀᴍ 10. ꜱʜɪᴋᴀᴍᴀʀᴜ ᴀꜱ ᴀɴ ᴀᴅᴜʟᴛ ꜱᴇʀᴠᴇꜱ ᴛʜᴇ ꜱᴇᴠᴇɴᴛʜ ʜᴏᴋᴀɢᴇ ᴀꜱ ᴀ ᴄʜɪᴇꜰ. ꜱʜɪᴋᴀᴍᴀʀᴜ ʜᴀꜱ ᴛʜᴇ ᴊᴜᴛꜱᴜ ᴏꜰ ᴄᴏɴᴛʀᴏʟʟɪɴɢ ᴛʜᴇ ꜱʜᴀᴅᴏᴡꜱ ᴏꜰ ᴏᴛʜᴇʀꜱ ᴀɴᴅ ʜɪᴍꜱᴇʟꜰ. ʜᴇ ᴜꜱᴇꜱ ᴀ ᴠᴀʀɪᴇᴛɪᴇꜱ ᴏꜰ ᴍᴏᴠᴇꜱ.
"""

disc3 = """
ꜱᴀᴅᴏ ʏᴀꜱᴜᴛᴏʀᴀ ᴀᴋᴀ ᴄʜᴀᴅ :  ᴄʜᴀᴅ ɪꜱ ᴀ ᴠᴇʀʏ ꜱᴋɪʟʟᴇᴅ ꜰɪɢʜᴛᴇʀ. ʜᴇ ʜᴀꜱ ꜱᴏᴍᴇ ᴀʙɪʟɪᴛɪᴇꜱ ᴄᴀʟʟᴇᴅ ᴛʜᴇ ꜰᴜʟʟʙʀɪɴɢ. ʜᴇ ᴄᴀɴ ᴍᴀᴋᴇ ʜɪꜱ ᴀʀᴍꜱ ꜱᴛʀᴏɴɢᴇʀ ᴀʟꜱᴏ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴘᴏᴡᴇʀꜱ ʟɪᴋᴇ ꜱʜɪᴇʟᴅ ᴀɴᴅ ʟɪɢʜᴛɪɴɢ ʙᴀꜱᴇᴅ ᴀᴜʀᴀ ꜱᴏ, ʜɪꜱ ᴘᴜɴᴄʜᴇꜱ ʜɪᴛꜱ ʜᴀʀᴅᴇʀ ᴛʜᴀɴ ʏᴏᴜʀ ᴅᴀᴅ'ꜱ ʙᴇʟᴛ.
"""



@Celestia.on_message(filters.command("character"))
async def character_creation(client, message):
    user_id = message.from_user.id

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴠɪᴠɪ", callback_data="vivi_"),
                InlineKeyboardButton("sᴀᴅᴏ", callback_data="sado_")
            ],
            [
                InlineKeyboardButton("sʜɪᴋᴀᴍᴀʀᴜ", callback_data="shikamaru_")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/55e27bacddf487d920a1a.jpg",
        caption="Choose your character:",
        reply_markup=keyboard
    )


@Celestia.on_callback_query(filters.regex(r'^vivi_$'))
async def vivi_(client, query):  
    keyboard = InlineKeyboardMarkup(
        [
            [ 
                InlineKeyboardButton("ᴄʜᴏᴏsᴇ", callback_data="choose_Vivi")
            ],
            [
                InlineKeyboardButton("◁", callback_data="sado_"),
                InlineKeyboardButton("▷", callback_data="shikamaru_"),
            ],
        ]
    )
    await query.message.edit_media(
        media=InputMediaPhoto("https://telegra.ph/file/83320930cef11dc2d598e.jpg",
                              caption=f"**📝 ɴᴀᴍᴇ**: ᴠɪᴠɪ\n**📈 ʟᴇᴠᴇʟ**: 1\n\n**ᴅᴇsᴄʀɪᴘᴛɪᴏɴ**: {disc1}"),
        reply_markup=keyboard
    )


@Celestia.on_callback_query(filters.regex(r'^shikamaru_$'))  # Corrected the callback data
async def shikamaru_(client, query):  # Added 'client' parameter
    keyboard = InlineKeyboardMarkup(
        [
            [ 
                InlineKeyboardButton("ᴄʜᴏᴏsᴇ", callback_data="choose_Shikamaru")
            ],
            [
                InlineKeyboardButton("◁", callback_data="vivi_"),
                InlineKeyboardButton("▷", callback_data="sado_"),
            ],
        ]
    )
    await query.message.edit_media(
        media=InputMediaPhoto("https://telegra.ph/file/ef9239db2ae67b44d4616.jpg",
                              caption=f"**📝 ɴᴀᴍᴇ**: sʜɪᴋᴀᴍᴀʀᴜ\n**📈 ʟᴇᴠᴇʟ**: 1\n\n**ᴅᴇsᴄʀɪᴘᴛɪᴏɴ**: {disc2}"),
        reply_markup=keyboard
    )


@Celestia.on_callback_query(filters.regex(r'^sado_$'))
async def sado_(client, query):  
    keyboard = InlineKeyboardMarkup(
        [
            [ 
                InlineKeyboardButton("ᴄʜᴏᴏsᴇ", callback_data="choose_Sado")
            ],
            [
                InlineKeyboardButton("◁", callback_data="shikamori_"),
                InlineKeyboardButton("▷", callback_data="vivi_"),
            ],
        ]
    )
    await query.message.edit_media(
        media=InputMediaPhoto("https://telegra.ph/file/4bc9e6bff0f863ff6a32a.jpg",
                              caption=f"**📝 ɴᴀᴍᴇ**: sᴀᴅᴏ\n**📈 ʟᴇᴠᴇʟ**: 1\n\n**ᴅᴇsᴄʀɪᴘᴛɪᴏɴ**: {disc3}"),
        reply_markup=keyboard
    )




    


@Celestia.on_callback_query(filters.regex(r'^choose_(Sado|Vivi|Shikamaru)$'))
async def choose_character_callback(client, query):
    user_id = query.from_user.id
    character_name = query.data.split('_')[1]

    users_data = {
        "name": character_name,
        "health": 100,
        "rank": "Novice Traveler",
        "partner": None,
        "experience": "[▰▱▱▱▱]1%",
        "level": 1,  
        "battel_win": 0,
        "total_bettel": 0,
        "player_id": user_id
    }

    users_collection.insert_one({str(user_id): users_data})
    await query.edit_message_text(f"You have chosen {character_name}! You can now use the /fight command.")



@Celestia.on_message(filters.command("profile"))
async def profile_command(client, message):
    user_id = message.from_user.id

    user_data = users_collection.find_one({"_id": str(user_id)})

    if not user_data:
        await message.reply("You haven't created a character yet. Use the /character command to create one.")
        return

    character_data = user_data
    user_profile = f"""
┏━━━━━━━━━━━━━━━━━
┣ Umm Player profile 
┗━━━━━━━━━━━━━━━━━
┏━⦿
┣⬢ Name : {character_data['name']}
┣⬢ Health : {character_data['health']}
┣⬢ Shells : 0
┣⬢ Player ID : {character_data['player_id']}  # Change 'player_id' to '_id'
┗━━━━━━━━━⦿

┏━⦿
┣ Exp : {character_data['experience']}
┣ Level : {character_data['level']}
┣ Rank : {character_data['rank']}
┣ Battles Win : {character_data['battle_win']}
┣ Total Battles : {character_data['total_win']}
┗━━━━━━━━━⦿
"""

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Family", callback_data="family_profile"),
         InlineKeyboardButton("Shop", callback_data="open_shop")]
    ])

    await message.reply_photo(
        photo="https://telegra.ph/file/55e27bacddf487d920a1a.jpg",
        caption=user_profile,
        reply_markup=reply_markup
    )



@Celestia.on_message(filters.command("deluser") & filters.user(SUDO_USERS))
async def delete_users(_, message):
    try:
        query = message.text.split(None, 1)[1]
        msg = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
        result = users_collection.delete_one({"_id": ObjectId(query)})

        if result.deleted_count == 1:
            await msg.edit("**ᴏʙᴊᴇᴄᴛ ɪᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ.**")
        else:
            await msg.edit("**ᴏʙᴊᴇᴄᴛ ᴅᴏᴇs ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ !!**")
    except Exception as e:
        await msg.edit(f"**ᴇʀʀᴏʀ**: {str(e)}")





