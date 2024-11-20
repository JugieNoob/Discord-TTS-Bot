import gtts
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(".", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    


@bot.command("tts")
async def self(ctx, msg:str):
    if (bot.voice_clients == []):
        await ctx.author.voice.channel.connect()
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    
    outputfile = gtts.gTTS(msg)
    outputfile.save("tts.mp3")
    voice_client.play(discord.FFmpegPCMAudio(source="assets/tts.mp3"))


load_dotenv()
bot.run(os.getenv("TOKEN"))