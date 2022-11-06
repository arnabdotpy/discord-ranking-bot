import discord
from discord.ext import commands
import json
import operator

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Leaderboard
    @commands.command(name = "leaderboard", aliases = ["lb","top"])
    async def leaderboard(self, ctx):
        try:
            with open("data.json","r") as f:
                file = json.load(f)
            tempDict = {}
            for i in file:
                tempDict[i] = file[i]["xp"]
            leaderboard = dict(sorted(tempDict.items(), key=operator.itemgetter(1), reverse=True))
            items = leaderboard.items()
            firstTen = list(items)[:10]
            dAgain = dict(firstTen)
            key = dAgain.keys()
            topList = list(key)
            embed=discord.Embed(color=0x8c52ff)
            embed.add_field(name="Leaderboard", value=f"""
    #1 - <@{topList[0]}>
    #2 - <@{topList[1]}>
    #3 - <@{topList[2]}>
    #4 - <@{topList[3]}>
    #5 - <@{topList[4]}>
    #6 - <@{topList[5]}>
    #7 - <@{topList[6]}>
    #8 - <@{topList[7]}>
    #9 - <@{topList[8]}>
    #10 - <@{topList[9]}>
    """, inline=False)
            embed. set_image(url="https://media.discordapp.net/attachments/870649335451361320/870944688545366057/Narrow_rgb_loading.gif")
            embed.set_footer(text = f"Requested by @{ctx.author}")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("Not enough data to show Leaderboard")

    #Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! `{round(self.bot.latency * 1000)}ms`") 

async def setup(bot):
    await bot.add_cog(cmd(bot))