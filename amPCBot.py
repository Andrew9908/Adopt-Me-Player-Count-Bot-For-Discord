import discord
from discord.ext import commands
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.roblox.com/games/920587237/Adopt-Me'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

client = commands.Bot(command_prefix = '!')
cmd1 = '!help'
cmd2 = '!amPC'
cmd3 = '!adoptmeplayercount'

@client.event
async def on_ready():
    print('Ready to count.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(cmd1):
        await message.channel.send('This bot is meant to count the number of players Adopt Me has. Use "!adoptmeplayercount" or "!amPC" to see the current number of people playing.')
    if message.content.startswith(cmd2) or message.content.startswith(cmd3):
        players = soup.get_text().partition("Playing")[2].partition("Favorites")[0]
        await message.channel.send('Adopt Me currently has ' + players + ' players! Wow!')

client.run('put token here')