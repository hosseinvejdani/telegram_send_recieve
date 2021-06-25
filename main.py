from pyrogram import Client, filters
import tracemalloc
tracemalloc.start()

def send_message(msg):
    app.send_message(channel_name, msg)


api_id = "2285336"
api_hash = "ce4084bb00243d6d9294e73550f5f6e4"
phone = "+989907160406"
username = "HosseinVejdani"
channel_name = 'SpinorApps'

app = Client(
    username,
    phone_number=phone,
    password='hvsh128',
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

print()


# @app.on_message(filters.channel('SpinorApps'))
# async def hello(client, message):
#     # await message.reply_text(f"Hello ...")
#     print(message)
#     print(type(message))
#     # print(help(message))
#     print(dir(message))
#     print('msg id ', message.message_id)
#     print('from user ', message.from_user)
#     print('text ', message.text)
#     print('views ', message.views)
#     fid = "AgACAgQAAx0EUSHeKQACGgFg1WBkA86_JE143YnwJslmfMa_XwAClLMxG5BMiVIEG-RTh5JC4NLs-ixdAAMBAAMCAAN5AAMTIAMAAR4E"
#     capt = "معجزات باورنکردنیه بغل کردن !\n\nبغل کردن معجزه میکند. یک آغوش گرم باعث ترشح دوپامین در مغز میشود که به هورمون لذت مشهور است. دقیقاً به همین خاطر است که فوراً احساس امنیت و آرامش میکنید. دانشمندان میگویند بغل کردن فشار خون و اضطراب را کاهش میدهد و روحیه را تقویت میکند\n\n@SpinorMag | اسپینور مگ"
#     await app.send_cached_media('SpinorApps', file_id=fid, caption=capt)


# app.run()





from pyrogram.handlers import MessageHandler


def my_function(client, message):
    # print(message)
    # print(type(message))
    # print(dir(message))
    print('msg id ', message.message_id)
    # print('from user ', message.from_user)
    # print('text ', message.text)
    # print('views ', message.views)
    if message['media']:
        capt = message['caption']
        caption_entities = message['caption_entities']
        capt = capt.replace(channels[message["sender_chat"]["username"]],'@SpinorMag')
        if message['photo']!=None:
            fid = message['photo']["file_id"]
            app.send_cached_media('spinor_mag', file_id=fid, caption=capt,caption_entities=caption_entities)
            
        if message['video']!=None:
            fid = message['video']["file_id"]
            app.send_cached_media('spinor_mag', file_id=fid, caption=capt,caption_entities=caption_entities)

        


my_handler = MessageHandler(my_function, filters.chat(list(channels.keys())))
app.add_handler(my_handler)

app.run()