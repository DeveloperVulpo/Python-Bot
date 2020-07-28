import discord
import os
from discord.ext import commands

TOKEN = open("token.txt", "r").readline()

client = commands.Bot(command_prefix=">")

# Ready Event
# Load all Cogs and consider yourself ready :)

@client.event
async def on_ready():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename[:-3]}")
    print("The Bot is Ready!")


# Load Command
# >load <Cog>

@client.command()
async def load(ctx, extention):
    client.load_extension(f"cogs.{extention}")
    await ctx.send(f"Loaded {extention}")

# Unload Command
# >unload <Cog>

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    await ctx.send(f"Unloaded {extention}")

# Reload Command
# >reload <Cog>

@client.command()
async def reload(ctx, extention):
    client.load_extension(f"cogs.{extention}")
    client.unload_extension(f"cogs.{extention}")
    await ctx.send(f"Unloaded {extention}")

# Say Command
# >say <message>

@client.command()
async def say(ctx, *, msg: commands.clean_content):
    await ctx.send(f"{msg}")

# Boa, Fiire I swear to god 👁️👄👁️
client.run(TOKEN)
