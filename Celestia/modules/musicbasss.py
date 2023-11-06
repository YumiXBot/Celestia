import pydub
from Celestia import Celestia
from pyrogram import filters



@Celestia.on_message(filters.command("bass") & filters.reply)
async def download_and_enhance_audio(client, message):
    try:
        reply_message = message.reply_to_message

        if reply_message.audio:
            audio = await reply_message.download()
            audio_segment = pydub.AudioSegment.from_file(audio)
            
            enhanced_audio = audio_segment + 10           
            enhanced_audio.export("enhanced_audio.ogg", format="ogg")
            
            await message.reply_audio("enhanced_audio.ogg")
        else:
            await message.reply("The replied message is not an audio.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")




