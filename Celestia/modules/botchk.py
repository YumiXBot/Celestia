import asyncio
from pyrogram import filters
from Celestia import Celestia, userbot

BOT_LIST = ["CelestiaXBot", "ZuliAiBot",]  # Replace with your bot usernames



@Celestia.on_message(filters.command("botschk"))
async def bots_chk(celestia, message):
    alive_bots = []
    dead_bots = []

    for bot_username in BOT_LIST:
        try:
            bot_info = await userbot.get_users(bot_username)
            alive_bots.append(bot_info)
        except Exception:
            dead_bots.append(bot_username)

    if alive_bots:
        alive_msg = "\n".join(f"✅ {bot.first_name} (ID: {bot.id}) is live" for bot in alive_bots)
        await celestia.send_message("Bots list with live:\n" + alive_msg)

    if dead_bots:
        dead_msg = "\n".join(f"❌ {bot_username} is dead" for bot_username in dead_bots)
        await celestia.send_message("Some bots are dead:\n" + dead_msg)



