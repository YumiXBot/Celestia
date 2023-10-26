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
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEAKQesQBKmk9aQfF8WXN8VehRCqn2OpSEKIkstvfYGENWXjvjOojBUKbY5h1aEXU0XYeyNb9osCNfVh1M2vX1qb1XS9t98-GZqFCtYyZce-eVathwGRnxGdcqyguGCa8JJJ4OVDTbQUsfaXb8OTtSNpcbC5Rg3hh7JxzumE47t-Yivz2uO95xgpBZ15hBibhljN8rOxRiYIrAScPdQJxulHgRAvC-CvZkQaIofgxW9uPIqg090bHVWm-pGkg1FEc5pdQ6t8SqBhFQUpjsgx_6eD0SNaQ-md6RB_hSopl8jGYFSSpWvClAB2gT0HubueNP5dTluvxpaWLXmH6euEwiMpQAAAAFsCkpbAA")
