from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/5203f8fcf8cad5ae816c0.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/4bad14b030d6b434116c2.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/xd_bots_support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/xd_bots_updates")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
