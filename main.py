import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import sys
import os

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)
should_stop = False
<<<<<<< HEAD

=======
>>>>>>> 2267c49302f7f42913594f8428d6274f3a0afbfe
@bot.event
async def on_ready():
    print("BOT IS READY")
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands")
    except Exception as e:
        print(f"An error with syncing commands: {e}")

@bot.tree.command(name="test", description="test command")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Test")

@bot.tree.command(name="poke", description="poke เรียกคนใน server")
@app_commands.describe(
    member="เลือกคนที่จะ poke",
    channel="เลือก channel ที่จะ poke",
    rounds="Number of pokes"
)
async def poke(interaction: discord.Interaction, member: discord.Member, channel: discord.VoiceChannel, rounds: int):
    global should_stop
    try:
        print("START DEFER")
        await interaction.response.defer(thinking=True)
        print("DEFER PASS")
        print("START CREATE BACKGROUND")
        asyncio.create_task(handle_poking(interaction, member, channel, rounds))
        print("CREATE BACKGROUND PASS")
    except Exception as e:
        print("ERROR : ", e)
        os.execv(sys.executable, ['python'] + sys.argv)
        should_stop = True

async def handle_poking(interaction: discord.Interaction, member: discord.Member, channel: discord.VoiceChannel, rounds: int):
    global should_stop
    should_stop = False

    if not member.voice or not member.voice.channel:
        try:
            await interaction.followup.send(f"{member.name} is not in a voice channel.", ephemeral=True)
        except discord.NotFound:
            print("Interaction or webhook no longer exists.")
        return

    if should_stop:
        return

    should_stop = False
    original_channel = member.voice.channel

    try:
        await interaction.followup.send(f"Start poking {member.name} for {rounds} rounds.", ephemeral=True)
    except discord.NotFound:
        print("Interaction or webhook no longer exists.")
        return

    try:
        for i in range(rounds):
            if should_stop:
                try:
                    await interaction.followup.send(f"Poking stopped at round {i}.", ephemeral=True)
                except discord.NotFound:
                    print("Interaction or webhook no longer exists.")
                break

            await member.move_to(channel)
            await asyncio.sleep(0.3)

            await member.move_to(original_channel)
            await asyncio.sleep(0.3)

            if (i + 1) % 10 == 0:
                try:
                    await interaction.followup.send(f"Poke ไปแล้ว {i + 1} รอบ...", ephemeral=True)
                except discord.NotFound:
                    print("Interaction or webhook no longer exists.")
                    break

        if not should_stop:
            try:
                await interaction.followup.send(f"Poke completed for {member.name}.", ephemeral=True)
            except discord.NotFound:
                print("Interaction or webhook no longer exists.")
    except Exception as e:
        try:
            await interaction.followup.send(f"An error occurred: {str(e)}")
        except discord.NotFound:
            print("Interaction or webhook no longer exists.")

@bot.tree.command(name="stoppoke", description="หยุด poke คน ใน server")
async def stoppoke(interaction: discord.Interaction):
    global should_stop
    should_stop = True
    await interaction.response.send_message("Poke has been stopped")


token = os.environ['DISCORD_TOKEN']
bot.run(token)
