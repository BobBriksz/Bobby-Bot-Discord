import discord
from os import getenv

BOT_TOKEN = getenv('BOT_TOKEN')

bot = discord.Client()

# event listener for when the bot has switched from offline to online
@bot.event
async def on_ready():
    #creates a counter to keep track of how many guils the bot is connected too
    guild_count = 0

    #loops through all the guild/servers that the bot is associated with
    for guild in bot.guilds:
        #print the servers id and name.
        print(f"-{guild.id} (name: {guild.name})")

        guild_count = guild_count+1
    print("BobbyBot is in "+ str(guild_count)+ " guilds")

#event listener for when a new message is sent to a channel

@bot.event
async def on_message(message):
    greetings = ['hello', 'hi', 'yo', 'sup', 'Hi bobby bot', 'whats good?', 'any gamers?']
    if message.content in greetings:
        #sends back a message
        await message.channel.send("hey Worm", tts=True)
# @bot.command()
# async def choose(ctx, *choices:str):
#     pass

bot.run(BOT_TOKEN)