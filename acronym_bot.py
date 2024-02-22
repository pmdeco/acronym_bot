import discord
import os

from dotenv import load_dotenv
from discord.ext import commands
from mikeisms import ROLE
from mikeisms import MIKEISMS

load_dotenv()
TOKEN = os.getenv("DECYPHMIKE_TOKE")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="&", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="status", help='Returns bot status')
async def status(ctx):
    await ctx.channel.send("I am alive.")
    await ctx.channel.send("My name is " + bot.user.name + ".")


@bot.event
async def on_message(message):
    parsed = set()
    await bot.process_commands(message)
    if message.author.id == bot.user.id:
        return
    roles = message.author.roles
    if ROLE in [y.name for y in message.author.roles]:
        words = message.content.split()
        for word in words:
            if word.upper() in MIKEISMS:
                parsed.add(word.upper())
        for e in parsed:
            if e in MIKEISMS:
                await message.channel.send(e + ": " + MIKEISMS.get(e))

bot.run(TOKEN)
