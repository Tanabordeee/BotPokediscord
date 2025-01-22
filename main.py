import discord
from discord.ext import commands
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

@bot.command()
async def test(ctx):
    await ctx.send("Test")

@bot.command()
async def poke(ctx, member: discord.Member, channel: discord.VoiceChannel, rounds: int):
    global should_stop
    if not member.voice or not member.voice.channel:
        await ctx.send(f"{member.name} is not in a voice channel.")
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
        await ctx.send(f"{member.name} has been poked {rounds} times")
    except Exception as e:
        await ctx.send(f"I can't move {member.name}. Error: {str(e)}")

@bot.command()
async def stoppoke(ctx):
    global should_stop
    should_stop = True
    await ctx.send("Poke has been stopped")
token = os.environ['DISCORD_TOKEN']
bot.run(token)
