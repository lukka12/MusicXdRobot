import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQB4ha-eQSP_J7-HlVPDGdg7gKu32tPdDwA8LgX-FUHLlq8TZLn-k6cgej5MBLBw_y6eqGmVTZm_rQrGQ5t4qgztUFFqBBVDt9IlMrxbQNY49VnhH2UEK2yYWL0xtD4HP9cbSBrjPitvIFqw_FdkfT3UKb7GRcdNVp8wXn9f-0sIF2BQyHvNFAD7yqnw6fxmcksZ_PokngmQIQSptSG9-XgubgbhVOzAkqX24pBnWQejRcW5qsQ1knkbN1u1GI-k0iZzcIhCxlSwdMKJXvNRjFuTm9YEIeIEzKyoE_D99zfy5DAH99gTv1hPI1CZQPvdE1XuQ91jWk6kyuskoiF_7FnTe27vYQA")
BOT_TOKEN = getenv("BOT_TOKEN", "2034558488:AAFCVz6rjcXEu1Opzyfny2oSMIuphk2SUlQ")
BOT_NAME = getenv("BOT_NAME", "𝙂𝙖𝙡𝙖𝙭𝙞𝙣𝙖 ✘ 𝙈𝙪𝙨𝙞𝙘")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/fb7d30e217de089621c87.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
admins = {}
API_ID = getenv("API_ID", "8755605")
API_HASH = getenv("API_HASH", "9d067982dcaa2f7020957036e2a1cb89")
BOT_USERNAME = getenv("BOT_USERNAME", "GalaxinaBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GalaxinaVcAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "WorldWideChatsXd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Sanki_BOTs")
OWNER_NAME = getenv("OWNER_NAME", "Chaii_Garam") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "Chaii_Garam")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "240"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2067182444").split()))
