import re
from pyrogram import Client, filters
from pyrogram.types import Message
from Celestia import Celestia
from http.client import HTTPConnection



@app.on_message(filters.command("bin"))
async def srbin(client, message: Message):
    BIN = message.text[len('.bin '):]
    reply_msg = message.reply_to_message

    if reply_msg:
        BIN = reply_msg.text

    try:
        _BIN = re.sub(r'[^0-9]', '', BIN)
        conn = HTTPConnection('binchk-api.vercel.app')
        conn.request('GET', f'/bin={_BIN}')
        response = conn.getresponse()
        if response.status == 200:
            data = response.read().decode()
            res = json.loads(data)
            msg = f'''
BIN: `{_BIN}`
Brand⇢ **{res["brand"]}**
Type⇢ **{res["type"]}**
Level⇢ **{res["level"]}**
Bank⇢ **{res["bank"]}**
Phone⇢ **{res["phone"]}**
Flag⇢ **{res["flag"]}**
Currency⇢ **{res["currency"]}**
Country⇢ **{res["country"]}({res["code"]})**
'''
            await message.edit(msg)
        else:
            await message.edit('Failed to parse bin data from api')
    except Exception as e:
        print(str(e))
        await message.edit('Failed to parse bin data from api')





