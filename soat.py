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
    soat = datetime.datetime.now(tz=ok)
    soat = soat.strftime("%H:%M")
    today = datetime.datetime.today()
    kun = today.strftime("%d")
    yil = today.strftime("%Y")
    oy = today.strftime("%m")
    oy = int(oy)-1
    month = ["yanvar","fevral","mart","aprel","may","iyun","iyul","avgust","sentabr","oktabr","noyabr","dekabr"]
    oy = month[oy]
    hafta = today.strftime('%w')
    hafta = int(hafta) - 1
    days = ["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]
    hafta = days[hafta]
    app.send(functions.account.UpdateProfile(
    first_name="Elbekjon ⏰ "+str(x),
    about="⌚️ Soat: " +str(soat) + " | 📆: " + str(kun) + "-" + str(oy) + " " + str(yil) + "-yil" + " | 🗓 Kun: " + str(hafta)
    ))
    time.sleep(20)
