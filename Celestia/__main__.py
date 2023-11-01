import asyncio
import importlib
from pyrogram import idle
from Celestia import Celestia
from Celestia.modules import ALL_MODULES
from Celestia.modules.Games import GAMES_MODULES

 

loop = asyncio.get_event_loop()


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Celestia.modules." + all_module)
     
    for game_module in GAMES_MODULES:
        importlib.import_module("Celestia.modules." + game_module)
      
    print("»»»» ʜᴇʀᴏᴋᴏ ʀᴏʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())
