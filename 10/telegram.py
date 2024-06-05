print('Міронова Євгенія,2 група, Лабораторна робота 6')
import getpass
import telethon
from telethon.errors import SessionPasswordNeededError


from telethon import TelegramClient
import re
import telethon.sync

api_id = 
api_hash = ""
username = ""
phone_number = ""

import pytz
from pytz import timezone
local_tz = timezone('Europe/Kiev')
#date = local_tz.localize(date)

with TelegramClient(username, api_id, api_hash) as client:
    client.start()

    channel_name = "cuterandomstuff"
    channel_entity = client.get_entity(channel_name)
    ch_date = channel_entity.date.replace(tzinfo=pytz.utc).astimezone(local_tz)
    print("ID каналу: {}\nusername каналу: {}\nНазва каналу: {}\nДата створення каналу: {}\n".format(
        channel_entity.id, channel_entity.username, channel_entity.title, ch_date))

    msgs = client.iter_messages(channel_entity, limit=5)
    for i, msg in enumerate(msgs):
        print("Пост #{}:".format(i+1))
        words = [word for word in msg.text.split() if re.search("[a-zA-Z]", word)]
        msg_date = msg.date.replace(tzinfo=pytz.utc).astimezone(local_tz)
        print("Дата й час публікації: {}\nЗміст:\n{}\nКількість знаків: {}\nКількість слів: {}\n".format(msg_date, msg.text, len(msg.text), len(msg.message.split())))

    msgs = client.iter_messages(channel_entity, reverse=True)
    with open("catss.txt", "w") as file:
        for msg in msgs:
            try:
                msg_date = msg.date.replace(tzinfo=pytz.utc).astimezone(local_tz)
                file.write(str(msg_date))
                file.write("\n")
                file.write(msg.text)
                file.write("\n\n\n\n")
            except TypeError:
                continue

print('Міронова Євгенія,2 група, Лабораторна робота 6')
import getpass
import telethon
from telethon.errors import SessionPasswordNeededError


from telethon import TelegramClient
import re
import telethon.sync

api_id = 111111111
api_hash = "xxxxxxxxxxxxxx"
username = "dnchn"
phone_number = "+38099999999"

import pytz
from pytz import timezone
local_tz = timezone('Europe/Kiev')
#date = local_tz.localize(date)

with TelegramClient(username, api_id, api_hash) as client:
    client.start()
