import discord
from discord.ext import commands
from os import getenv

BOT_TOKEN = getenv('BOT_TOKEN')

client = commands.Bot(command_prefix="-")

# event listener for when the bot has switched from offline to online
@client.event
async def on_ready():
    #creates a counter to keep track of how many guils the bot is connected too
    guild_count = 0

    #loops through all the guild/servers that the bot is associated with
    for guild in client.guilds:
        #print the servers id and name.
        print(f"-{guild.id} (name: {guild.name})")

        guild_count = guild_count+1
    print("BobbyBot is in "+ str(guild_count)+ " guilds")

#event listener for when a new message is sent to a channel

@client.event
async def on_message(message):
    greetings = ['hello', 'hi', 'yo', 'sup', 'Hi bobby bot', 'whats good?', 'any gamers?']
    if message.content in greetings:
        #sends back a message
        await message.channel.send("hey Worm", tts=True)
    if message.content == 'milkies':
        await message.channel.send("Mommy milkies. I want mommy milkies. Big Mommy Milkies. I love mommy Milkies", tts=True)
# @bot.command()
# async def choose(ctx, *choices:str):
#     pass

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency *1000)}ms')
    
client.run(BOT_TOKEN)