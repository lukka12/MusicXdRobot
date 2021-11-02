import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCiI7KGR4Qrosebn857-QvDqQNoIitfoPzKLOTBEnRu8k4OmjcW0LWA2URSKE556A7X0RAMhlLfGNXWVMRaXtWBAZi9KjmMAVv7Qk4ac0uaJW_j7mKfx1QEPkjBLz9aVfYVp78Xd8sdOe9BB40lz9vrk9FCx_EGfEdLgPQAL0952QeQUQk5KVE24QRyoYMd7PmXZvVWfhho1zSjL5l0V8joWejU6OCN9e9jQfUetcK5PBq4GHEw9LYb-3EaO-R6Lblmk1Y1DcMWih71p5COq9HfYsV1q6SLn7jyP7Nenf3ZrtM70phulYJASs8GatpCLjLmBnqg3vQH023ctMDS7LZge27vYQA")
BOT_TOKEN = getenv("BOT_TOKEN", "2034558488:AAFCVz6rjcXEu1Opzyfny2oSMIuphk2SUlQ")
BOT_NAME = getenv("BOT_NAME", "𝙂𝙖𝙡𝙖𝙭𝙞𝙣𝙖 ✘ 𝙈𝙪𝙨𝙞𝙘")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/fb7d30e217de089621c87.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
admins = {}
API_ID = int(getenv("8755605"))
API_HASH = getenv("9d067982dcaa2f7020957036e2a1cb89")
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
