import gtts
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(".", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # Create channel.txt if it does not exist.
    if not os.path.exists("channel.txt"):
        with open("channel.txt", "w") as file:
            pass
        print("Created channel.txt")
        
    

async def playTTS(ctx, msg:str):
    # Check if bot is connected to a voice channel.
    if (bot.voice_clients == []):
        try:
            # Connect bot to the voice channel and deafen itself.
            await ctx.author.voice.channel.connect(self_deaf=True)
        except:
            await ctx.send("Could not connect to voice channel. Please make sure you are in a voice channel.")
            return
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    
    print(voice_client)
    
    outputfile = gtts.gTTS(msg)
    outputfile.save("tts.mp3")
    # Play the inputted message.
    voice_client.play(discord.FFmpegPCMAudio(source="tts.mp3"))



@bot.command("tts")
async def self(ctx, msg:str):
    await playTTS(ctx, msg)
    # Add a reaction to the message
    await ctx.message.add_reaction("🗣️")

@bot.command("config")
async def self(ctx, channel:discord.TextChannel = None):
    ttschannel = ""
    try:
        with open("channel.txt", "r") as file:
            # Get the channel id.
            ttschannel = file.readline()
    except:
        print("Could not find channel.txt!")
    
    
    if channel is not None:
        try:
            with open("channel.txt", "w") as file:
                    # Set the channel id.
                    file.write(str(channel.id))
                    print("Wrote new channel id to channel.txt")
                    await ctx.send(f"Set TTS channel to <#{channel.id}>")
        except:
            await ctx.send("Could not set TTS channel. Did you specify a channel?")
    else:
        if ttschannel == "":
            await ctx.send(f"No TTS channel is set!")
        else:
            await ctx.send(f"The current TTS channel is <#{ttschannel}>")
    

@bot.event
async def on_message(msg):
    ttschannel = ""
    try:
        with open("channel.txt", "r") as file:
            # Get the channel id.
            ttschannel = file.readline()
    except:
        print("Could not find channel.txt!")
    
    # If there is a tts channel and the message was not sent from the bot, play the TTS message.
    if ttschannel != "" and not msg.author.bot:
        if msg.channel.id == int(ttschannel):
            await playTTS(msg, msg.content)       
            # Add a reaction to the message
            await msg.add_reaction("🗣️")
    


    # Stops the bot from breaking.
    await bot.process_commands(msg)
    
# Start the bot.
load_dotenv()
bot.run(os.getenv("TOKEN"))
