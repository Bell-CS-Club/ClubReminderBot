import discord
from discord.ext import commands

def get_mentions(ctx):
    members_mentioned = set()
    members_mentioned.update(ctx.message.mentions)
    for role in ctx.message.role_mentions:
        members_mentioned.update(role.members)
    return members_mentioned

async def dm(ctx, members, msg):
    members_msg = []
    for member in members:
        if (member not in members_msg) and (not member.bot):
            try:
                print(f'Sending message from {ctx.author.mention} to {member.mention}...\n')
                await member.send(msg.content)
            except:
                pass
            members_msg.append(member)
            #print(members_msg)
            #print('')
    print('--------------------------------------------------------\n')
    await msg.reply('Message(s) sent.')

