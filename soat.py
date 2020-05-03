from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
api_id = 1302700 #my.telegram.org dan olgan apiidni qoying
api_hash = "8314d027824113f071171e1680267bfe" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    today = datetime.datetime.today()
    y = today.strftime("%m/%d/%Y")
    app.send(functions.account.UpdateProfile(
    first_name="Elbekjon ⏰ "+str(x),
    about="O'zbekistonda soat: " +str(x) + " kun: " + str(y)
    ))
    time.sleep(20)
