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
    voice_client.play(discord.FFmpegPCMAudio(source="tts.mp3"))

@bot.command("config")
async def self(ctx, channel:discord.TextChannel):
    try:
        with open("channel.txt", "w") as file:
                file.write(str(channel.id))
                print("Wrote new channel id to channel.txt")
                await ctx.send(f"Set TTS channel to <#{channel.id}>")
    except:
        await ctx.send("Could not set TTS channel. Did you specify a channel?")


    
load_dotenv()
bot.run(os.getenv("TOKEN"))
