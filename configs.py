from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "29909260"))
    API_HASH = getenv("API_HASH", "b50fc1417139325122a146ef588ec212")
    BOT_TOKEN = getenv("BOT_TOKEN", "6342724900:AAE40893igCQNJ6fHsvLHnI8dQF3GBVdvW0")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", ""))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://autochannelfilter:autochannelfilter@cluster0.mcpsuva.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
