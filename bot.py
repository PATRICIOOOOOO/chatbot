import discord
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.messages = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$cat'):
        cat_emoji = "😺"
        await message.channel.send(cat_emoji)
    else:
        await message.channel.send(message.content)

client.run("¡EL TOKEN DE TU BOT DEBERÍA ESTAR AQUÍ!")
