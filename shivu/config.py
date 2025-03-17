import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LOGGER = True
    
    # Configuration depuis les variables d'environnement
    OWNER_ID = os.getenv("OWNER_ID")
    sudo_users = os.getenv("OWNER_ID") # même que OWNER_ID par défaut
    TOKEN = os.getenv("BOT_TOKEN")
    mongo_url = os.getenv("MONGO_URL")
    PHOTO_URL = ["https://i.imgur.com/ErTVdOY.jpeg"]  # vous pouvez garder ceci en dur ou le déplacer dans .env
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT")
    UPDATE_CHAT = os.getenv("UPDATE_CHAT")
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    CHARA_CHANNEL_ID = os.getenv("CHARA_CHANNEL_ID")
    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")

class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True
