import discord
from discord.ext import commands
from discord import app_commands
import requests
import json
import asyncio

#---------- Informations require for the bot ----------#
token = ''
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
    
# Main function
async def delta_key(interaction, hwid):
    await interaction.response.defer(thinking=True)

    if hwid.startswith('https://gateway.platoboost.com/a/8?id='):
        hwid = hwid.replace('https://gateway.platoboost.com/a/8?id=', '')

    code = "cacc"

    payload = {
        "captcha":"",
        "type":""
    }

    session = requests.Session()
    session.post(f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{hwid}", json=payload)
    await asyncio.sleep(5)
    session.put(f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{hwid}/{code}")
    response = session.get(f"https://api-gateway.platoboost.com/v1/authenticators/8/{hwid}").text

    try:
        await interaction.followup.send(content=json.loads(response)["key"])
    except:
        await interaction.followup.send(content="Failed.")

#--- Get Delta Key ---#
@bot.tree.command(description="Get delta key.")
@app_commands.describe(
    hwid='Enter your ID'
)
async def key(interaction: discord.Interaction, hwid: str):
    await delta_key(interaction, hwid)


#---------- Bot's events ----------#
#--- Log on ---#
@bot.event
async def on_ready():
    #--- Sync commands ---#
    await bot.tree.sync()
    print(f'Logged on as {bot.user}')

#--- Handle command not found ---#
@bot.event
async def on_command_error(ctx, error):
    pass

#---------- Run bot ----------#
bot.run(token)
