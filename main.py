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

@client.command()
async def msg_role(ctx, *roles):
    if not ctx.message.role_mentions:
        await ctx.reply("Mention roles nerd.")
        return
    
    await ctx.reply("What is your message?")
    def get_msg(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        msg = await client.wait_for('message', timeout=20.0, check=get_msg)
    except asyncio.TimeoutError: #oh yea don't forget to add asyncio to requirements.txt
        await ctx.reply('Enter a message or practice your typing speed.')
        return
    
    members_msg = []
    for role in ctx.message.role_mentions:
        for member in role.members:
            if (member not in members_msg) and (not member.bot):
                try:
                    print(f'Sending message from {ctx.author.mention} to {member.mention}...') #debugging ig idk how to debug
                    await member.send(msg.content)
                except:
                    pass
            members_msg.append(member)
            print(members_msg) #debugging ig idk how to debug
    
if __name__ == "__main__":
    client.run(os.getenv("DISCORD_TOKEN"))
