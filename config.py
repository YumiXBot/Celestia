import os
from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "CelestiaXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "5997219860:AAGstFLBkn1NZ6GlgTLulOdsfPxplIzPQQs")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819 6691393517 5465943450").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Hiroko:Hiroko@cluster0.1hztkgz.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEASZs4Gx8ldmZ4usHpaOL_fzqvqVGdEV_GURyHGczzbvQSqAXyydlv-kt9O_C0cF9F1Gzh3MWLQNZ-ls1icSZKPexNlOryzXO9WyTYPwlUjt5_cUc3Z61xwuZ7jtJ5uVvW6nUdiF-LsE7a3-xuUmKdbRomeLbd-xDBOgx7fX7bt7oevzOIfmYXD1H-GX4-q990O346iPVwJNfZxF9yna19lsfqf_e2aLo38HrB7NywWYnzebhPIiVupCs67VMnGg8WnCbQXR4eHbxilIRiEL7mwywsyn5PGQtrNMvil8HrFor8dbrZQ-nJTAXeVVe1Pkox0wKhjq5g9ik8cRZvz9rffAAAAAFsCkpbAA")
