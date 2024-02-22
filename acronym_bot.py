import discord
import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DECYPHMIKE_TOKE")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="&", intents=intents)

MIKEISM = {
	# Ranks
    "1STLT" : "1st Lieutenant",
	"1STSGT": "First Sergeant",
	"2NDLT" : "2nd Lieutenant",
	"BGEN"	: "Brigadier General",
	"COL"	: "Colonel",
	"CPL"	: "Corporal", 
	"CWO2"	: "Chief Warrant Officer 2",
	"CWO3"	: "Chief Warrant Officer 3",
	"CWO4"	: "Chief Warrant Officer 4",
	"CWO5"	: "Chief Warrant Officer 5",
	"E1"	: "Private",
	"E2"	: "Private First Class",
	"E3"	: "Lance Corporal",
	"E4"	: "Corporal",
	"E5"	: "Sergeant",
	"E6"	: "Staff Sergeant",
	"E7"	: "Gunnery Sergeant",
	"E8"	: "Master Sergeant or First Sergeant",
	"E9"	: "Master Gunnery Sergeant or Sergeant Major or Sergeant Major of the Marine Corps",
	"LCPL"	: "Lance Corporal",
    "LT"	: "Lieutenant",
	"LTCOL" : "Lieutenant Colonel",
	"LTGEN"	: "Lieutenant General",
    "LTS"	: "Lieutenants",
	"MAJGEN": "Major General",
	"MGYSGT": "Master Gunnery Sergeant",
	"MSGT"	: "Master Sergeant",
	"O1"	: "Second Lieutenant",
    "O2" 	: "First Lieutenant",
    "O3" 	: "Captain",
    "O4" 	: "Major",
    "O5" 	: "Lieutenant Colonel",
    "O6" 	: "Colonel",
    "O7" 	: "Brigadier General",
    "O8" 	: "Major General",
	"O9"	: "Lieutenant General",
	"O10"	: "General",
	"PFC"	: "Private First Class",
	"PVT"	: "Private",
	"SGTMAJ": "Sergeant Major",
	"SGT"	: "Sergeant",
	"SMMC"	: "Sergeant Major of the Marine Corps",
	"SSGT"	: "Staff Sergeant",
	"W1"	: "Warrant Officer",
	"W2"	: "Chief Warrant Officer 2",
	"W3"	: "Chief Warrant Officer 3",
	"W4"	: "Chief Warrant Officer 4",
	"W5"	: "Chief Warrant Officer 5",
	"WO"	: "Warrant Officer",
    "29"	: "paradise",
    "96"	: "four days of vacation",
    "0802"	: "https://tenor.com/view/running-away-genitals-dildo-pink-dildo-gif-14469419",
    "ADJ"	: "adjunct who supports provides admin support for the commander",
    "BC"	: "battery commander",
    "BN"	: "battalion",
    "CO"	: "commanding officer",
	"ISLC"	: "Infantry Squad Leaders Course",
    "MOS"	: "military occupational specialty",
    "MQ9"	: "Reaper Drone",
    "NLT"	: "No Later Then",
    "OIC"	: "Officer In Charge",
    "OPCON"	: "operational control",
    "OPFOR"	: "opposing force",
    "OPSO"	: "operations officer",
    "PCS"	: "Permanent Change of Station",
    "PCSING": "Permanent Change of Station, i.e., moving",
	"PICMDEEP": "Principles of Machine Gun Employment: (1) Pairs, (2) Interlocking Fires, (3) Coordination of Fire,  (4) Coordination in the Offense, (5) Coordination in the Defense, (6) Mutual Support, (7) Defilade, (8) Enfilade, (9) Economy, (10) Protection",
    "POG"	: "person other than grunt",
    "TBS"	: "The Basic School",
    "XO"	: "executive officer"
}

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
    if "USMC" in [y.name for y in message.author.roles]:
        words = message.content.split()
        for word in words:
            if word.upper() in MIKEISM:
                parsed.add(word.upper())
        for e in parsed:
            if e in MIKEISM:
                await message.channel.send(e + ": " + MIKEISM.get(e))

bot.run(TOKEN)
