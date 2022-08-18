#Kuzey Ceylan Tarafindan Yapilmistir Baska Hesapta Paylasılamaz.

import os
import random
import time
import json

with open("resource/data.json") as loadjson:

    paneldata = json.load(loadjson)


class renkler:
    PEMBE = '\033[95m'
    MAVI = '\033[94m'
    CAMGOBEGI = '\033[96m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    DUZ = '\033[0m'
    KALIN = '\033[1m'
    ALTICIZILI = '\033[4m'


print(renkler.CAMGOBEGI + "Welcome To Admin Panel.")
while True:
    password = input(renkler.KALIN + "Password: ")

    if password != paneldata["$PassWord"]:
        print(renkler.KIRMIZI + "PassWord Is Not True!")
        time.sleep(1)

        if os.name == "nt":
            os.system("cls")

        if os.name == "posix":
            os.system("clear")

    elif password == paneldata["$PassWord"]:
        print(renkler.YESIL + "PassWord Is True!")
        time.sleep(1)

        if os.name == "nt":
            os.system("cls")

        if os.name == "posix":
            os.system("clear")
        #Burdan Sonrasina Panel Komutlari Ekleyebilirsin.
