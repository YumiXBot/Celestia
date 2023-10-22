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
SESSION_STRING = getenv("SESSION_STRING", "BQBnHjY97pLO30lOWLJnuersAhW8LiFhcKymqGUguUrEjJOc6p1agZ6tgo5OFHVAJxqnlAAzAJNL4qHJiCRQurv9a0VXX02h2ZW0ohgoyIpwcWkNqsL0ThZJRCuhjth67T3-59nFaaauYUXvTx5xqpy0C_Jinlj_GutFBvzv06x6yNA5ibEK8ZvPOMWq-aD5y82-j6nZwR_xb-ZL-sDIYfSslN-FJI0t5eqq9DfMz_31iQaSVyTIcfbvsgIIni8O_VUeeUqa-3awI1a4iHbVSa1a6t6KaCuDnk2CN9Xx8VO8AdIkMO4HbOtjSg9umAZwNARQ9By23-heXpbPt3uTJGAAAAAWwKSlsA")
