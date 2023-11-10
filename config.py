from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "CelestiaXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6711389550:AAHYtV97shWhg7UrtjTGWqDru6bH812aBtk")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819 6691393517 737932898 6610172048 2072367717").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Celestia:Celestia@celestia.08chke4.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEAR50pjELSfjwLsEelea470c7zwVwuurZd_PU-IofxmES3UzzyltxGIF-ZGPk8Z6-2Uf_rxpw4rVfbMPtnLovBYSDQvznrL7ffRUy_Hpvt4W7jbNlCZ7bZ4y7oLvhcc2jdvhD0m_ch5xQqDc5dq6rr8luwjvgwTqqcwK081MDANqE2EcJNkJNa2CvE4KViyU7Zs8RuHlkMnldDZwSp4jgIPxwxeTlgPaUZqdVRQE_8KUB7gYMJJ71s45Zw3yD0TfvhycwRX1Wqv5kZHdyF_I2miEbWxmpN7LE9a38qRRmhxeOijX0Ld-QSwI3sLTxyKbhlICbtxZoF66nv2EYO_vUIKAAAAAFsCkpbAA")

