import os

try:
    from pypresence import Presence
except:
    if input("Install dependencies? [y/n]: ").lower() == 'y':
        os.system('pip -r requirements.txt')

from datetime import datetime
import time 
import json
import extras

os.system("cls")
os.system("title YourWay Presence")

def load_settings():
    with open("settings.json" , "r") as f:
        settings = json.load(f)

    return settings

settings = load_settings()


RPC = Presence(client_id=settings["client-id"])
RPC.connect()

if settings["start_time"] == 0:
    start_time = time.time()

else:
    start_time = settings["start_time"]

if settings["time"] == True and settings["button"] == True:
    RPC.update(buttons = settings["buttons"] , large_image=settings["large-image"] , large_text=settings["large-image-text"] , details=settings["details"], state=settings["state"] , start=start_time)

elif settings["time"] == False and settings["button"] == True:
    RPC.update(buttons = settings["buttons"], large_image=settings["large-image"] , large_text=settings["large-image-text"] , details=settings["details"] , state=settings["state"])

elif settings["time"] == False and settings["button"] == False:
    RPC.update(large_image=settings["large-image"] , large_text=settings["large-image-text"] , details=settings["details"] , state=settings["state"])

elif settings["time"] == True and settings["button"] == False:
    RPC.update(large_image=settings["large-image"] , large_text=settings["large-image-text"] , details=settings["details"] , state=settings["state"] , start=start_time)

print("Please check your rich presence on discord!")

while True:
    time.sleep(5)
