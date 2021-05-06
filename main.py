import discord
from discord.ext import commands
import os

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


if __name__ == "__main__":
    client.run(os.getenv("DISCORD_TOKEN"))
