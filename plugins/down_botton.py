from pyrogram.types import ReplyKeyboardMarkup
from pyrogram import Client, filters


@Client.on_message(filters.command("start") 
async def start_txt(client, message):
    await message.reply_text(
        text="Hi Bro how are U", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "Start 😘"
            ]]
        ) 
    ) 
