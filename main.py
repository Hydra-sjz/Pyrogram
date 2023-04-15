import pyrogram
import os
from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)



class bot(Client):
    
    def __init__(self):
        super().__init__(
            name="musicdl",
            bot_token=BOT_TOKEN,
            api_id=API_ID,
            api_hash=API_HASH,
            workers=20,
            plugins=dict(
                root="plugins"
            )
        )

if __name__ == "__main__" :
    bot().run()
