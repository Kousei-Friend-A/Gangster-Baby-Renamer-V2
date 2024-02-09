import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = "5098785902:AAFmvndi6bs_cop5XcT_1_xsHCpzGG6t_iQ"

API_ID = int(os.environ.get("API_ID", "8143727"))

API_HASH = "e2e9b22c6522465b62d8445840a526b1"

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
