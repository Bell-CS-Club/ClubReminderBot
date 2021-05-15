import discord
from discord.ext import commands
import os
import asyncio

import bot_functions as bot

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="$", intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user.id}")


@client.event
async def on_message(message):
    await client.process_commands(message)


@client.command()
async def owo(ctx):
    await ctx.send("owo")


@client.command()
async def hello(ctx):
    await ctx.send("World!")


@client.command()
async def shutdown(ctx):
    await ctx.send("Shutting down!")
    await client.close()


@client.command()
async def msg(ctx, *, mentions):
    
    members_msg = bot.get_mentions(ctx)
    
    if not members_msg:
        await ctx.reply("Mention someone nerd.")
        return
    
    await ctx.reply("What is your message?")
    def get_msg(message):
        return message.author == ctx.author and message.channel == ctx.channel
    try:
        msg = await client.wait_for('message', timeout=20.0, check=get_msg)
    except asyncio.TimeoutError:
        await ctx.reply('Bro enter a message or practice your typing speed.')
        return
    
    await bot.dm(ctx, members_msg, msg)


if __name__ == "__main__":
    client.run(os.getenv("TOKEN"))