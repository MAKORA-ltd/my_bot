class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5650073623"
    sudo_users = "5650073623"
    GROUP_ID = "-1002335396984"
    TOKEN = "7850896694:AAFr8xYWn158CZ97FXE8cO5r8QM6DWWxjd4"
    mongo_url = "mongodb+srv://enam:enam2025@cluster0.rploi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://i.imgur.com/ErTVdOY.jpeg"]
    SUPPORT_CHAT = "@maKorachatAccess"
    UPDATE_CHAT = "@makoraUpdate"
    BOT_USERNAME = "@makorA_bot"
    CHARA_CHANNEL_ID = "-1002493620336"
    api_id = "21831396"
    api_hash = "40dee31c5c60d66363c3837b7f69de89"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
