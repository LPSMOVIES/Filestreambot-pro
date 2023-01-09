# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '25712813'))
    API_HASH = str(getenv('API_HASH', 'c201751b80c7d185f986141cbadc4275'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5649345445:AAEALDSlFIFTAxJxpsdE3JzfIBySuTKEnjU'))
    name = str(getenv('name', 'filetolink_lsbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '30'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001518497631'))
    PORT = int(getenv('PORT', 8888))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '192.46.215.23'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5493968060").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'logesh_bots'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '192.46.215.23:8888') if not ON_HEROKU or getenv('FQDN', '192.46.215.23:8888') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Logesh:Logesh2004@cluster0.xjdaatq.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Logeshbots'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
