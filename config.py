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
SESSION_STRING = getenv("SESSION_STRING", "BQCy_fH3XRDIS8ryaQ0QByw5YsSXBuEcv9VtZSjT1N8HJl9qWgdFNlOtDYq9UM8lqMLjnKoRsP8Yee3aosbnmV6kxZQ7dY5c_AUTld_lN8EQj0l2od9yamr0zjxRdmHUEZtfjdAn3c3fLru3gZ3RDDfHRO8bDyb0xx3TOk6LD9bwvchSDB4y5LN8IwWnqe8wp4Tv6TjA7FH_C7yfVvdN1AGMJkbfz3NGMOvxihfQqI8Ap8KM1J3NhHP5wOgQqOWaBOAr46sedP3jqYeuWSrQEr9s2_u1jGGj1nD_yE5Df5IcKm_1_X6hK8mnN3EagWBwEkhFFDzEgN1j7Qdio8dacBAAAAAWwKSlsA")
