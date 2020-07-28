import discord
from discord.ext import commands

class Information(commands.Cog):
    def __init__ (self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"🏓 Pong, Latency: {round(self.client.latency * 1000)}ms")


def setup(client):
        client.add_cog(Information(client))
