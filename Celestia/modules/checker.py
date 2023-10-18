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



def generate_credit_card(bin, count=10):
    card_numbers = []
    bin_length = len(bin)
    if bin.isdigit() and bin_length == 6:
        for _ in range(count):
            cc = bin + "".join([str(random.randint(0, 9)) for _ in range(10)])
            date = "".join([str(random.randint(0, 2)]) + str(random.randint(0, 9)])
            year = "".join([str(random.randint(2, 2)]) + str(random.randint(5, 9)]) # Ensure year is not greater than 2029
            cvv = "".join([str(random.randint(0, 9)) for _ in range(3)])
            card_info = f"{cc}|{date}|{year}|{cvv}"
            card_numbers.append(card_info)
        return card_numbers
    return []



@Celestia.on_message(filters.command("gencc"))
async def generate_credit_cards(client, message):
    if len(message.text.split()) == 2:
        bin = message.text.split()[1]
        card_numbers = generate_credit_card(bin)
        if card_numbers:
            text = "Generated Credit Card Numbers:\n\n"
            for card_info in card_numbers:
                text += f"{card_info}\n"
            reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Generate More CC", callback_data="gencc")]]
            )
            await message.reply_text(text, reply_markup=reply_markup)
        else:
            await message.reply_text("Invalid format. Use: /gencc 736373")
    else:
        await message.reply_text("Invalid command. Use: /gencc 736373")


@Celetia.on_callback_query(filters.regex("gencc"))
async def generate_cc_callback(client, callback_query):
    await callback_query answer()
    message = callback_query.message
    bin = message.text.split('\n')[1].split()[2]
    card_numbers = generate_credit_card(bin)
    if card_numbers:
        text = "Generated Credit Card Numbers:\n\n"
        for card_info in card_numbers:
            text += f"`{card_info}`\n"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Generate More CC", callback_data="gencc")]]
        )
        await message.reply_text(text, reply_markup=reply_markup)







