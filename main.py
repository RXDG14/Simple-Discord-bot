import discord
import os
import random
##########################################################################
from discord.ext import commands
#file = "c://Users/Rakshit/Desktop/kekw.png"

bot = commands.Bot(command_prefix='t?', case_insensitive=True)

@bot.command(name='hello', description="Greet the user!")
async def hello(ctx, user: discord.User = None):
    if not user:
        user = ctx.author
    await ctx.send(f"Hello {user.name} :thumbsup: :thumbsup: :thumbsup: ")#<:love:735913338239975465:> <:love:735913338239975465:>

@bot.event
async def on_message(message):
    if "hi" in message.content.lower():
        await message.channel.send(f"Hello {message.author.name}")
    if "hello" in message.content.lower():
        await message.channel.send(file=discord.File('kekw.png'))

    await bot.process_commands(message)
bot.run('ODMxNTIzODQyNDIwNzY4ODA4.YHWe7A.OhsWx02txgeIyotza5n4BP-BtvI')
