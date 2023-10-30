import os
from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "CelestiaXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "5997219860:AAGstFLBkn1NZ6GlgTLulOdsfPxplIzPQQs")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819 6691393517").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Hiroko:Hiroko@cluster0.1hztkgz.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEAF45gxT-8DUZuzAGT05noqf-H3OlVD0VJ2jYbL97p6it_JAZ0Ekrici7LPYtgFdGPN1G7b_U4gbJN1w4rYVq-IYWSL37M5VtB8dw-3YhYDlQFAXkV0MRIwe6CAljsazZ5HF-iJuBFkzLZF2fUEC_pk8e4wvN4jyut2uVs6UukdJj9PDx-pzkwXdsdd-I4Z3sTgGCT2J2Wsc0YxCcCehbSc__TyTEGNGYfQaFF8hbkxXkw0GUlqCeC35pOGKxbt1-jM5lK4UksW4HVNeBq10tLoJ6ee9wMv6Tf9rYtVdV1LVn63FEeVhQmxr5QF3ytsly8PbKBVpFbGXX3EYUhQ2kPTgAAAAFsCkpbAA")
