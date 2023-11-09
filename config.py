from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "CelestiaXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6711389550:AAHYtV97shWhg7UrtjTGWqDru6bH812aBtk")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819 6691393517 737932898 6610172048").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Celestia:Celestia@celestia.08chke4.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEAYBbawqbirpX95RDZtB-SdgNR5TwaWF66dHq9PpNoVWSpkK8RgSJxuPcEAMHfD_XUE0blmZX3sh0bbzduK4OBYUqcfjQ9SEanKzMPp2qhFyRs6aD7C9Jai2or8iLwUjypnHr-qqdbgdPYQGUIp0cTM_gpOhqmwr0mJP4rUOkw8Z7ugcWBth_4YSgdM-hn3Mhn9Jrc22pSAlaN_Rk8KJkCu8lTrFJ72dCGhpkozgl5SrpYzbL0mStDryUIVTVpLWk5tkPVSh5dbiZZsvSxEfYIqgW3jWHEMHry65tvT9B5JP_hAAJZ0YDhhchR56SAJZSLALpz68XWQuwy4jyrIbj-KgAAAAFsCkpbAA")

