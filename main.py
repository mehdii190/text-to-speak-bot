##### import #####

from os import getenv
from pyrogram import Client
from dotenv import find_dotenv , load_dotenv
from googletrans import Translator
import pyttsx3

## Code ##
load_dotenv(find_dotenv())
    ## <********>
app = Client("app",api_id=int(getenv("api_id")),api_hash=getenv("api_hash"),bot_token=getenv("token"))
    ### *** ###
print("bot is run...")
    ### (*) ###
## Message Translator ##

@app.on_message()
async def main(Client,message):

    
    user = message.from_user.id
    text = message.text
    trans = Translator()
    trans2 = trans.translate(text,"es")
    print(trans2.text)
    await message.reply(trans2.text)
    voice(trans2.text)
    await app.send_audio(user,"voice.mp3")

## Create Voice mp3 ##

def voice(text):
    engine = pyttsx3.init()
    engine.save_to_file(text,"voice.mp3")
    engine.runAndWait()
    return engine


# Bot work #

app.run()

    #########$$$$$ ID TEL $$$$$$######
    #########> mehdi_190_mmm <########