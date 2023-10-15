from pyrogram import Client, filters
import requests
from Celestia import Celestia


@Celestia.on_message(filters.command("start"))
def start_command(client, message):
    chat_id = message.chat.id
    username = message.from_user.username
    message_id = message.message_id
    client.send_message(
        chat_id,
        f"─ Switchblade Checker Panel ─\n⁕ Registered as ➞ @{username}\n⁕ Use ➞ /cmds to show available commands.\n⁕ Owner ➞ @pentagrvm | Update Logs ➞ @switchbladeupdate",
        reply_to_message_id=message_id
    )

@Celestia.on_message(filters.command("cmds"))
def cmds_command(client, message):
    chat_id = message.chat.id
    client.send_message(
        chat_id,
        "─ Switchblade Commands ─\n\n➣ Stripe Charge/Auth [✅]\nUsage: /chk cc|mm|yy|cvv\n\n➣ Check SK Key [✅]\nUsage: /key sk_live\n➣ Check Info [✅]\nUsage: /info\n➣ Check BIN Info [✅]\nUsage: /bin xxxxxx\nContact → @pentagrvm"
    )

@Celestia.on_message(filters.regex(r'^/(bin|!bin|\!bin|\.bin) (.+)$'))
def bin_check_command(client, message):
    chat_id = message.chat.id
    username = message.from_user.username
    message_id = message.message_id

    bin = message.matches[0].group(1)
    bin = bin[:6]

    response = requests.get(f"https://lookup.binlist.net/{bin}")
    data = response.json()

    bank = data.get("bank", {}).get("name", "")
    name = data.get("name", "")
    brand = data.get("brand", "")
    country = data.get("country", {}).get("name", "")
    scheme = data.get("scheme", "")
    emoji = data.get("emoji", "")
    card_type = data.get("type", "")

    message_text = f'⁕ ─ 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ✅ ─ ⁕\nBIN: {bin}\nBANK: {bank}\n𝙲𝙾𝚄𝙽𝚃𝚁𝚞: {name}  ({emoji})\nBRAND: {brand}\nCARD: {scheme}\nTYPE: {card_type}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nCHECKED BY: @{username}'

    client.send_message(
        chat_id,
        message_text,
        reply_to_message_id=message_id,
        parse_mode="html"
    )

@Celestia.on_message(filters.command(["info", "id"]))
def info_id_command(client, message):
    chat_id = message.chat.id
    username = message.from_user.username
    firstname = message.from_user.first_name

    if message.text == "/info":
        info_text = f"⁕ ─ 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 ─ ⁕\nChat ID: {chat_id}\nName: {firstname}\nUsername: @{username}"
    else:
        info_text = f"Chat ID: {chat_id}"

    client.send_message(
        chat_id,
        info_text,
        parse_mode="html"
    )


import random

def random_ua():
    tipos_disponiveis = ["Chrome", "Firefox", "Opera", "Explorer"]
    tipo_navegador = random.choice(tipos_disponiveis)
    
    if tipo_navegador == 'Chrome':
        navegadores_chrome = [
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
            # Add other Chrome user agents here
        ]
        return random.choice(navegadores_chrome)
    
    elif tipo_navegador == 'Firefox':
        navegadores_firefox = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
            'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
            # Add other Firefox user agents here
        ]
        return random.choice(navegadores_firefox)
    
    elif tipo_navegador == 'Opera':
        navegadores_opera = [
            "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
            'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
            # Add other Opera user agents here
        ]
        return random.choice(navegadores_opera)
    
    elif tipo_navegador == 'Explorer':
        navegadores_ie = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            # Add other Internet Explorer user agents here
        ]
        return random.choice(navegadores_ie)


import requests

def GetStr(string, start, end):
    start_index = string.find(start)
    end_index = string.find(end, start_index)
    if start_index != -1 and end_index != -1:
        return string[start_index + len(start):end_index]
    return ""

def check_credit_card_info(message):
    if message.startswith("!chk") or message.startswith("/chk"):
        message = message[5:]
        cc, mes, ano, cvv = message.split("|")

        # Bin Look-up using binlist.net
        bin_url = f'https://lookup.binlist.net/{cc}'
        headers = {
            'User-Agent': 'Your User Agent',
        }
        response = requests.get(bin_url, headers=headers)
        bin_data = response.json()
        bank = bin_data['bank']['name']
        name = bin_data['name']
        country = bin_data['country']['name']
        emoji = bin_data['emoji']
        scheme = bin_data['scheme']
        card_type = bin_data['type']
        currency = bin_data['currency']

        if 'credit' in scheme.lower():
            # Perform actions for credit cards
            pass

        # Bin Look-up using binlist.io
        bin = cc[:6]
        bin_url = f'https://binlist.io/lookup/{bin}'
        response = requests.get(bin_url)
        bin_data = response.json()
        scheme = bin_data['scheme']
        country = bin_data['country']['name']
        card_type = bin_data['type']
        bank = bin_data['bank']['name']

        # Perform further actions with the obtained information

if __name__ == '__main__':
    message = input("Enter the message: ")
    check_credit_card_info(message)



import requests
import random

# Generate Random User Data using randomuser.me API
random_user_api_url = 'https://randomuser.me/api/1.2/?nat=us'
response = requests.get(random_user_api_url)
data = response.json()
user = data['results'][0]

name = user['name']['first']
last = user['name']['last']
email = user['email']
street = user['location']['street']
city = user['location']['city']
state = user['location']['state']
phone = user['phone']
postcode = user['location']['postcode']

# Proxy Configuration
proxies = {
    1: 'socks5://p.webshare.io:1080',
    2: 'http://p.webshare.io:80',
}
selected_proxy = proxies[random.choice(list(proxies.keys()))]

proxy_user_pwd = 'YourProxyUsername:YourProxyPassword'  # Replace with your proxy credentials

# Check the IP address using the selected proxy
ipify_url = 'https://api.ipify.org/'
response = requests.get(ipify_url, proxies={'http': selected_proxy, 'https': selected_proxy}, auth=(proxy_user_pwd))
ip_address = response.text

if response.status_code == 200:
    ip_status = "Proxy live"
else:
    ip_status = f"Proxy Dead: [{selected_proxy}]"

print(f"Name: {name} {last}")
print(f"Email: {email}")
print(f"Street: {street}")
print(f"City: {city}")
print(f"State: {state}")
print(f"Phone: {phone}")
print(f"Postcode: {postcode}")
print(f"IP Address: {ip_address}")
print(f"IP Status: {ip_status}")


import requests
from pyrogram import Client, filters

# Create a Pyrogram client
app = Client("stripe_bot")

# Define a command handler to process /chk commands
@app.on_message(filters.command("chk"))
async def check_card(bot, message):
    # Split the command message to extract card details
    _, card_details = message.text.split(" ", 1)
    card_number, exp_month, exp_year, cvv = card_details.split("|")

    # Your Stripe API Key
    stripe_api_key = "YOUR_STRIPE_API_KEY"

    # Construct the API request data
    data = {
        "card[number]": card_number,
        "card[exp_month]": exp_month,
        "card[exp_year]": exp_year,
        "card[cvc]": cvv,
        "key": stripe_api_key,
    }

    try:
        # Make a POST request to Stripe API
        response = requests.post("https://api.stripe.com/v1/tokens", data=data)

        if response.status_code == 200:
            result = response.json()
            if "error" in result:
                error_message = result["error"]["message"]
                await message.reply(f"Stripe Error: {error_message}")
            else:
                await message.reply("Stripe Payment Successful")
        else:
            await message.reply("Stripe Payment Failed")

    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run()


from pyrogram import Client
import requests

api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
phone_number = "YOUR_PHONE_NUMBER"

# Create a Pyrogram client
with Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number) as app:
    message = "YOUR_MESSAGE"
    
    if message.startswith(("/key", "!key", ".key")):
        sec = message[4:]
        url = 'https://api.stripe.com/v1/tokens'
        data = {
            'card[number]': '5278540001668044',
            'card[exp_month]': '10',
            'card[exp_year]': '2024',
            'card[cvc]': '252'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': sec
        }
        
        response = requests.post(url, data=data, headers=headers)
        result = response.text
        
        if 'api_key_expired' in result:
            app.send_message("YOUR_CHAT_ID", f"⁕ ─ 𝗦𝗞 𝗞𝗘𝗬 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ─ ⁕\nKEY: <code>{sec}</code>\nMESSAGE: Expired API key Provided.\n𝚂𝚃𝙰𝚃𝚄𝚂: DEAD ❌\n𝙲𝙷𝙴𝙲𝙺𝙴𝙳 𝙱𝚈: @{app.get_me().username}", parse_mode="html")
        elif 'Invalid API Key provided' in result:
            app.send_message("YOUR_CHAT_ID", f"⁕ ─ 𝗦𝗞 𝗞𝗘𝗥𝗬 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ─ ⁕\nKEY: <code>{sec}</code>\nMESSAGE: Invalid API Key Provided.\n𝙲𝙷𝙴𝙲𝙺𝙴𝙳 𝙱𝚈: @{app.get_me().username}", parse_mode="html")
        elif 'You did not provide an API key.' in result or 'You need to provide your API key in the Authorization header,' in result:
            app.send_message("YOUR_CHAT_ID", f"⁕ ─ 𝗦𝗞 𝗞𝗘𝗬 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ─ ⁕\nMESSAGE: You did not provide an API key.\n𝙲𝙷𝙴𝙲𝙺𝙴𝙳 𝙱𝚈: @{app.get_me().username}", parse_mode="html")
        elif 'testmode_charges_only' in result or 'test_mode_live_card' in result:
            app.send_message("YOUR_CHAT_ID", f"⁕ ─ 𝗦𝗞 𝗞𝗘𝗬 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ─ ⁕\nKEY: <code>{sec}</code>\nMESSAGE: Testmode Charges Only.\n𝚂𝚃𝙰𝚃𝚄𝚂: DEAD ❌\n𝙲𝙷𝙴𝙲𝙺𝙴𝙳 𝙱𝚈: @{app.get_me().username}", parse_mode="html")
        else:
            app.send_message("YOUR_CHAT_ID", f"⁕ ─ 𝗦𝗞 𝗞𝗘𝗬 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ─ ⁕\nKEY: <code>{sec}</code>\nMESSAGE: SK Key Live.\n𝚂𝚃𝙰𝚃𝚄𝚂: LIVE ✅\n𝙲𝙷𝙴𝙲𝙺𝙴𝙳 𝙱𝚈: @{app.get_me().username}", parse_mode="html")










