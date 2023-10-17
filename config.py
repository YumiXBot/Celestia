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
SESSION_STRING = getenv("SESSION_STRING", "BQCDVW2vV3VsK0j0u1EdpNJScSy-A4W5mT6RlaJXh7VhOv_PJC4ogMU63a4MAvdkdmFqHMYIoLG5ZbPq94zX9FBBtNnzFQ_QMzpfYSaDJ911_3USx6zx8_tu3ykjIVXy_PG3ZEXI8x6mdlBHBYU2Omx4ZqLqSBpMU5xT5Q2jyVeAKV07up2wSjqfeYoEJvVw025CMbhqFjNE-y1EHaMCguDo1bvTBHcbq8f2LJh9rFb4Tc6sgfYHReR2OGUVya3qktt1l3JiJO5m3Sh803G9FCjpQUizB133wfIlntK9iOS6ignKxqGW482FjGCw0RbhUhm0OIDTocaGyIW3YobTL2n0AAAAAWwKSlsA")
