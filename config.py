from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "CelestiaXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6711389550:AAHYtV97shWhg7UrtjTGWqDru6bH812aBtk")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819 6691393517 737932898 6610172048 2072367717").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Celestia:Celestia@celestia.08chke4.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEAThG1rb9QGHlQTLq1qsFCRqw2T4Lp4Ve_sPKxxbQUIM8JyqMJR2yg_pMwAXE8Hd1PtzKwK7zRRR7loY5WrN4V0jQ4VDE2t21RvzF-AOR5eRRF0Avdzxsg7okYihzYR4tyKwQ5tCx7n_u8FU7K8DLqqqProkgTM9j-16QZj-q9H0LrPkDm3agvZ8dH_fa0gGw_jcAWqYO6Y-BHIkri5_ngKsnL_0xifirki1p-Aj7P3GcBXmmsGmqq0JzrfLQ29B6orgvwZp6rURpFX9M5y66n50rTL7WbpD7whyq8L7RrcCZwYMDdrHo8GrTJB2SK0UyB80UcR-GJ-CKJnFPiKYPk6QAAAAFsCkpbAA")

