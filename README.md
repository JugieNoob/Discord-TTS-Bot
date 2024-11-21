# Discord TTS Bot 🎤

## Table of Contents 📝
- [What is this ❓](#what-is-this-question)
- [Showcase 📺](#showcase-tv)
- [Dependencies 📃](#dependencies-page_with_curl)
- [How to Setup ℹ️](#how-to-setup-information_source)
- [Commands ⌨️](#commands-keyboard)

##  What is this :question:

This Discord bot allows you to play TTS messages in the voice channel you are currently in.

- If you encounter any problems with the bot please make an issue [here](https://github.com/JugieNoob/Discord-TTS-Bot/issues) and i will try my best to solve them.

# Showcase :tv:
### 1. Configuring the TTS channel.
![Configuring the TTS channel](/imgs/1.png)

### 2. Checking which TTS channel is configured.
![Checking which TTS channel is configured](/imgs/2.png)

### 3. Using the TTS command.
![Using the TTS command](/imgs/3.png)

### 4. Sending messages in the configured TTS channel.
![Sending messages in the configured TTS channel](/imgs/4.png)

## Dependencies :page_with_curl:
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [pythondotenv](https://pypi.org/project/python-dotenv/)
- [gTTS](https://pypi.org/project/gTTS/)

❗To install the dependencies type ``pip install -r requirements.txt`` into a terminal window. ❗

## How to Setup :information_source:

Please click [here](https://github.com/JugieNoob/Simple-Discord-Mod-Bot/blob/main/Setup.md) to learn how to setup and start the bot.


## Commands :keyboard:

Command|Description
-|-
.tts | Plays a TTS message in the voice call (you must be in a call for this to work
.config | Tells you which text channel is currently being listened to for messages.
.config {text-channel} | Starts listening to the the inputted text channel for messages.
