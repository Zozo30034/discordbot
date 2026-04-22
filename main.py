import discord
from discord.ext import commands
import os

# 1. Rechte (Intents) festlegen
intents = discord.Intents.default()
intents.message_content = True  # Erlaubt dem Bot, Nachrichten zu lesen

# 2. Bot-Präfix festlegen (z.B. !hallo)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'ZACK! Der Bot ist live als {bot.user}')

@bot.command()
async def hallo(ctx):
    await ctx.send('Moin! Dein Python-Bot läuft 24/7 auf Railway! 🐍🚀')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latenz: {round(bot.latency * 1000)}ms')

# 3. Den Token von Railway abrufen
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
