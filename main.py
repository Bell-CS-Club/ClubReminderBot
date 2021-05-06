import discord
from discord.ext import commands
import os

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '$', intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    await client.process_commands(message)

@client.command()
async def owo(ctx):
    if ctx.author == client.user:
        return
    
    else:
        await ctx.send("owo")

client.run(os.getenv("DISCORD_TOKEN"))
