import os, time, requests
import openai, g4f
from pyrogram import filters
from Celestia import Celestia
from pyrogram.enums import ChatAction, ParseMode
from gtts import gTTS





openai.api_key = "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"




@Celestia.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(celestia :Celestia, message):
    
    try:
        start_time = time.time()
        await celestia.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.ask How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            await message.reply_text(f"{x}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        




@Celestia.on_message(filters.command(["deep"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(celestia: Celestia, message):
    try:
        await celestia.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
                "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-** Please provide text after the .deep command"
            )
        else:
            a = message.text.split(' ', 1)[1]

            data = {
                'text': a,  
            }

            headers = {
                'api-key': '9133bea4-ddf1-40d0-bcac-089e0fbacb4f',
            }

            r = requests.post("https://api.deepai.org/api/text-generator", data=data, headers=headers)
            response = r.json()
            answer_text = response['output']
            await message.reply_text(f"{answer_text}")
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")





@Celestia.on_message(filters.command(["bing"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(celestia :Celestia, message):
    
    try:
        start_time = time.time()
        await celestia.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.bing How to set girlfriend ?`")
        else:
            query = message.text.split(' ', 1)[1]
            response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": query}],  
            provider=g4f.Provider.Bing
            )
            await message.reply_text(f"{response}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        






@Celestia.on_message(filters.command(["assis"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(celestia :Celestia, message):
    
    try:
        start_time = time.time()
        await celestia.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.assis How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            text = x    
            tts = gTTS(text, lang='en')
            tts.save('output.mp3')
            await celestia.send_voice(chat_id=message.chat.id, voice='output.mp3')
            os.remove('output.mp3')            
            
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        

