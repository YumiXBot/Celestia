import os
from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "CelestiaXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "5997219860:AAGstFLBkn1NZ6GlgTLulOdsfPxplIzPQQs")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Hiroko:Hiroko@cluster0.1hztkgz.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEAJFimS9sgw-I65ryfvAHm3q42WtWSiwhsEOs8dW080ngSBk0kOTtl9tCfpb1OU_0yU5Z2typ9qwLxafN7-R_r69uSUGlMx4f_GAGrBT03f0FeeCOYpiaMPF0iGCep9Oc3HAqMflosN8JpzwtEzN-eJHqAiIqw3hy6RF7BkG03lNBu4SO8-2uaq-vj0VEUn8ZjND017kmmgQKgpW2BDc_XTjLsUGPQCn28GKNuIPbBBIgPgqLnnSqi9niMoExQJ8bwsX-OYK0GmYkCmkni1aGrOS8xkLGzrSD233xPYe-YVlXYaI0KX1mxrlIp8hagWg0O9mkU0QCCmT7GXEMLjScTiAAAAAFsCkpbAA")
