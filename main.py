import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("BOT IS READY")
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands")
    except Exception as e:
        print(f"An error with syncing commands",e)
@bot.tree.command(name="test" , description="test command")
async def test(interaction:discord.Interaction):
    await interaction.response.send_message("Test")

@bot.tree.command(name="poke" , description="poke เรียกคนใน server")
@app_commands.describe(
    member="เลือกคนที่จะ poke",
    channel="เลือก channel ที่ะตจ",
    rounds="Number of pokes"
)
async def poke(interaction:discord.Interaction, member: discord.Member, channel: discord.VoiceChannel, rounds: int):
    global should_stop
    if not member.voice or not member.voice.channel:
        await interaction.response.send_message(f"{member.name} is not in a voice channel.")
        return
    should_stop = False
    original_channel = member.voice.channel   
    try:
        for _ in range(rounds):
            if should_stop:
                break
            await member.move_to(channel) 
            await asyncio.sleep(1)        
            await member.move_to(original_channel) 
            await asyncio.sleep(1)     
    except Exception as e:
         await print(f"I can't move {member.name}. Error: {str(e)}")

@bot.tree.command(name="stoppoke", description="หยุด poke คน ใน server")
async def stoppoke(interaction:discord.Interaction):
    global should_stop
    should_stop = True
    await interaction.response.send_message("Poke has been stopped")
token = os.environ['DISCORD_TOKEN']
bot.run(token)
