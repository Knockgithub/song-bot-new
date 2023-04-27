import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "27535343"))
    API_HASH = os.environ.get("API_HASH", "06766128d68d9c1a0d683ecfbb91de2f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6078574846:AAFl2EyoQt7SaunI0TlU-1bOsOIIhdjDzGI")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2a35fca576aa49de77c98.jpg")
    OWNER = os.environ.get("OWNER", "shamilhabeeb") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
