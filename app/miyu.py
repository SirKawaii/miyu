# bot.py
import os
import requests
import discord
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# prefix
prefix = "!miyu"

# messages
bienvenida = "Hola!, los comandos disponibles son:  \' ip \' "

def get_ip():
    ip = requests.get('https://api.ipify.org?format=json')
    if(ip.status_code == 200):
        content = json.loads(ip.content)
        return f"La IP del server actual es : {content['ip']}"
    else:
        return "Algo paso con la Api de ip, intentalo de nuevo mas tarde por favor uwu"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        command = message.content.replace(prefix, '', 1).strip()
        print(f'command text [{command}]')
        if command == '':
            await message.channel.send(bienvenida)

        if command == ('hola'):
            await message.channel.send('¿Como estás? Espero tengas un buen día.')

        if command == 'ip':
            await message.channel.send(get_ip())

client.run(TOKEN)
