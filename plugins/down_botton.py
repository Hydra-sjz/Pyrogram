from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram import Client, filters


@Client.on_message(filters.command("start")) 
async def start_txt(client, message):
    await message.reply_text(
        text="Hi Bro how are U", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "Start 😘", " Help😌", "About 🥲"
            ],[
                "🎵 Music Galaxy 🎵"
            ],[
                "YouTube 🔴", " Spotify 🟢", "Deezer 🟣"
            ],[
                "Close ❌"
            ]]
            resize_keyboard=True, 
        ) 
    ) 


@Client.on_message(filter.reggex("Start 😘"))
async def start_myr(client, message):
    await message.reply_text(
        text="Start", 
    ) 

@Client.on_message(filter.reggex("Close ❌"))
async def close_myr(client, message):
    await message.reply_text(
        text="Botton Close", 
        reply_markup=ReplyKeyboardRemove() 
    ) 
        
        
