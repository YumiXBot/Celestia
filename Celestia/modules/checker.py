from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from Celestia import Celestia


def generate_card_number(starting_digit, length):
    card_number = str(starting_digit)
    for _ in range(length - 1):
        card_number += str(random.randint(0, 9))
    return card_number

starting_digits = {
    "Visa": 4,
    "Mastercard": 5,
    "American Express": 3,
    "Discover": 6
}



@Celestia.on_message(filters.command("genbin"))
async def generate_card_numbers(client, message):
    # Generate 10 random card numbers for each card type
    random_card_numbers = {}
    for card_type, starting_digit in starting_digits.items():
        random_card_numbers[card_type] = [generate_card_number(starting_digit, 6) for _ in range(10)]

    # Create a message with card numbers
    text = ""
    for card_type, card_numbers in random_card_numbers.items():
        text += f"`{card_type} Card Numbers`:\n"
        for card_number in card_numbers:
            text += f"`{card_number}`\n"
        text += "\n"

    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Generate Again", callback_data="genbins")]]
    )
    await message.reply_text(text, reply_markup=reply_markup)



@Celestia.on_callback_query(filters.regex("genbins"))
async def generate_callback(client, callback_query):
    # Generate more card numbers when the "Generate Again" button is pressed
    try:
        await callback_query.answer("generating....")
        message = callback_query.message
        await generate_card_numbers(client, message)
    except Exception as e:
        await callback_query.answer("oops error")
        error_message = f"An error occurred: {str(e)}"
        await message.reply_text(error_message)



# ======================= gen cc ==============================


