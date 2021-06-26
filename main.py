from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import json
import tracemalloc
tracemalloc.start()

def send_message(msg):
    app.send_message('SpinorApps', msg)

# ===========================================================
# info.json containes telegram account informations like this:
# {
#     "api_id" : "xxxxxxx",
#     "api_hash" : "xxxxxxxxxxxxxxxxxxxxxxxx",
#     "phone" : "+989xx716xxxx",
#     "username" : "xxxx",
#     "password" : "xxxxxxx"
# }
# you shoud make a info.json in the main directory with
# your own telegram account infos
f = open('info.json',)
info = json.load(f)
f.close()
api_id = info['api_id']
api_hash = info['api_hash']
phone = info['phone']
username = info['username']
password = info['password']

app = Client(
    username,
    phone_number=phone,
    password=password,
    api_id=api_id,
    api_hash=api_hash
)

channels={}
channels['Ajibvalivaghaei'] = '@Ajibvalivaghaei'
channels['factpedia'] = '@factpedia'
channels['danstany_ajib'] = '@danstany_ajib'
channels['Dansstaniha'] = '@Dansstaniha | دانستنی ها ™'
channels['Ajayebe_jahann'] = '@Ajayebe_jahann'
channels['mytestchch'] = '@mytestchch'
channels['irWonders'] = '@irWonders'

file_ids = []

def my_function(client, message):
    print('msg id ', message.message_id)
    if message['media']:
        capt = message['caption']
        caption_entities = message['caption_entities']
        if '@'+message["sender_chat"]["username"] in capt:
            capt = capt.replace(channels[message["sender_chat"]["username"]],'@SpinorMag')
            if message['photo']!=None:
                fid = message['photo']["file_id"]
                if not fid in file_ids:
                    file_ids.append(fid)
                    app.send_cached_media('SpinorMag', file_id=fid, caption=capt,caption_entities=caption_entities)
                
            if message['video']!=None:
                fid = message['video']["file_id"]
                if not fid in file_ids:
                    file_ids.append(fid)
                    app.send_cached_media('SpinorMag', file_id=fid, caption=capt,caption_entities=caption_entities)

    

my_handler = MessageHandler(my_function, filters.chat(list(channels.keys())))
app.add_handler(my_handler)

app.run()