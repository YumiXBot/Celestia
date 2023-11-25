from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "NottyyXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6808170222:AAEy7kiRfRoppFJMCW8c2a-3D4yYlzJ5D6E")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6079943111").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Celestia:Celestia@celestia.08chke4.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQB5s0xYnXYBiDhhrlptdMKf7P7hDNuM0HYXsdwjc3_ykz-akPwtzkpCMDYnMBce3aAEsTooDJfS7LXCc5rE47d6SYuO5h6D71TwKpWgr6WNvZhI7VYIB_39gRQ8pHif6FRqIui6lHE9UDYpuGjJmCOGOczAg18jZbvVrMTET5EpNEog0M4EPn2R8WtS_d82Z12bnZVQrLKMzwReMwkKrDWqXwiRyfl8lVkkdtCk0NFKcBp3p1jrCPJUIFfZ9hgtStNwht52m56aJVUlgtXHQ7krrXw-PcJR7lZspDbRFEbZTOKkCL3nLh-Pujio-y05cQbDTUa-ScVbliwKYmVHgbgEAAAAAVKUpfgA")

