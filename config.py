import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH")

CHANNEL_MAPPING = {
    -1002386644256: -1002484982348,
    -1001597273610: -1001721796359,
    -1002261820786: -1002255696539,
    -1002418710282: -1002292610792,
    -1002100804603: -1002334248978,
    -1002698179276: -1002492502401,
}

ALLOWED_MIME_TYPES = {"video/x-matroska", "video/mp4"}
