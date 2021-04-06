#!/usr/bin/env python3

import discord

BOT_TOKEN = "<TOKEN>"
TARGET_ID = <AUTHOR_ID>

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if(message.author.id == TARGET_ID):
            if("Wanna play with me ?" in message.content):
                await message.channel.send("yes")
            elif("Is that okay ?" in message.content):
                await message.channel.send("yes")
            elif("Daniel Ricciardo" in message.content):
                await message.channel.send("Perth")
            elif("Barack Obama" in message.content):
                await message.channel.send("08/04/1961")
            elif("Gal Gadot" in message.content):
                await message.channel.send("Israeli")
            elif("Omar Sy" in message.content):
                await message.channel.send("43")
            elif("Billie Eilish" in message.content):
                await message.channel.send("Billie Eilish Pirate Baird O'Connell")
            elif("best CTF" in message.content):
                await message.channel.send("P'HackCTF")

client = MyClient()
client.run(BOT_TOKEN, bot=False)