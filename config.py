from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "NottyyXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6808170222:AAEy7kiRfRoppFJMCW8c2a-3D4yYlzJ5D6E")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6079943111").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Celestia:Celestia@celestia.08chke4.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQFnEL8AJByW47kYbdzI3P0Q1zJu31g19F2l2lSh8-bM9B_sSLCR-VHNvI50NZp2GKF_uX-eMFDOoL7iSi1CDmk5NhfkDk6YXwDM8gmoAEKhZPFI8F8g11wR7PLvVGAIjL8bsdHmwwCJQT7KvhHGjPcVrF_7ziHEGQ5HIZrDCiwpd8ylc7xFsw4ygfrcj2SKyFzlFMDQrkOLBSVU3caDfIhR0Lz78L8I003HWnrIMFRnpWecYl8ZYPDFRBS3LheDk6QA8tRLu83SA4_xOJyCDOTGg83a1m0obUdlgnEvK20pfBz-g2sBUXtkwcIWWeGogUAmqwQvKii8zm0f2lakT8lpGpNEPgAAAAFTXiDAAA")

