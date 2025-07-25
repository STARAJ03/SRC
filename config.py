# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""
img_url = getenv("img_url","https://imgs.search.brave.com/THqPKczwvPZMcP7ME81cY86Y_zf3C5TvrUIkce6YNCo/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9yMi5z/dGFycnlhaS5jb20v/cmVzdWx0cy8xMDA3/MzQ3OTcwLzk2NzVj/YjQzLWE4YmEtNGYy/Ny05NmU5LTYzYTNk/NzVlYTQ5Zi53ZWJw")
Credit = getenv("Credit","Star AJ")
c_url = getenv("c_url","https://t.me/+N5xSRah10TZlNmY1")
API_ID = int(getenv("API_ID", "27765349"))
API_HASH = getenv("API_HASH", "9df1f705c8047ac0d723b29069a1332b")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1116405290").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002409813500")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002409813500"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "indianshortner.com")
AD_API = getenv("AD_API", "2c1a1a8b45d35782b595c0a645b4d03694b937d0")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
