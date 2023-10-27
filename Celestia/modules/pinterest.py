import requests
from bs4 import BeautifulSoup
import json
from requests import get 
from Celestia import Celestia
from pyrogram import filters
from pyrogram.types import InputMediaPhoto



@Celestia.on_message(filters.command(["image", "generate", "photo"]))
async def pinterest(_, message):
     chat_id = message.chat.id

     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

     images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

     media_group = []
     count = 0

     msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")
     for url in images["images"][:6]:
                  
          media_group.append(InputMediaPhoto(media=url))
          count += 1
          await msg.edit(f"=> ᴏᴡᴏ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

     try:
        
        await Celestia.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()

     except Exception as e:
           await msg.delete()
           return await message.reply(f"ᴇʀʀᴏʀ : {e}")
          
     



@Celestia.on_message(filters.command(["chichi"]))
async def playgrounai(_, message):
    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    url = f"https://playgroundai.com/search?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        htmlcontent = response.content
        soup = BeautifulSoup(htmlcontent, "html.parser")
        script_tag = soup.find("script", id="__NEXT_DATA__")

        if script_tag:
            json_data = json.loads(script_tag.contents[0])
            data_list = json_data['props']['pageProps']['data']

            images = []
            max_images = 10

            for item in data_list:
                if 'url' in item:
                    images.append(item['url'])
                    if len(images) >= max_images:
                        break

            media_group = [InputMediaPhoto(url) for url in images]

            try:
                msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ chichi...")
                await Celestia.send_media_group(message.chat.id, media=media_group)
                await msg.delete()
            except Exception as e:
                await msg.delete()
                return await message.reply(f"ᴇʀʀᴏʀ : {e}")

        else:
            return await message.reply("No data found with ID '__NEXT_DATA__'")

    else:
        return await message.reply(f"Failed to retrieve the webpage. Status code: {response.status_code}")









