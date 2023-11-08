from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "CelestiaXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6711389550:AAHYtV97shWhg7UrtjTGWqDru6bH812aBtk")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819 6691393517 6050277919").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Celestia:Celestia@celestia.08chke4.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEAwtFxgQx_syjUYFa9-O4poM3cV5cFO3nxsFCYvk-d64SEzNBCNGLZb4YmpxTfITV90uJ5fh6SjZ256Txphd5L9tZ8o93jYfUBXGRvXwylwdejfOGj4T2XxHdiXCZORwabnHwhN1rIEjHA2LgGTj4Cn8SE2CtV423GK8s3NQP52PzIUy_s2opXGHnovVARvVln1I5MPv6sItpfDxencV7IdTfM2SCyxPZ1SVAknYHG048lZB8PjhayR_i1uR9Ps8GxzbVhUZKlvoRHDOHHAA1iqY3MerX9aVcow_CPj4Ck8OnApruEBdczvJdvf60TdB3B_jq_N7IuESbkLIXxz5VBfgAAAAFsCkpbAA")

