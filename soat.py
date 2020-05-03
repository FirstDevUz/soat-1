from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
api_id = 1302700
api_hash = "8314d027824113f071171e1680267bfe"
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    today = datetime.datetime.now(tz=ok)
    soat = today.strftime("%H:%M")
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
    first_name="🇺🇿 #FirstDev ⏰ "+str(soat),
    about="⏰ " +str(soat) + " | 📆 " + str(kun) + "-" + str(oy) + " | 📅 " + str(yil) + "-yil" + " | 🗓 " + str(hafta) + " | 📝 Pyrogram profile"
    ))
    time.sleep(20)
