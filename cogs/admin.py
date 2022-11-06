import discord
from discord.ext import commands
import json

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Add XP
    @commands.command()
    async def add(self, ctx, user:discord.Member = None):
        if ctx.author.guild_permissions.administrator:
            if user is None:
                user = ctx.author
            with open("data.json", "r") as f:
                user_data = json.load(f)
            id = user.id
            await ctx.send("How many xp do you want to increase?")
            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel
            msg = await ctx.bot.wait_for("message", check=check)
            xp = msg.content
            if str(id) in user_data:
                user_data[str(id)]["xp"] = user_data[str(id)]["xp"] + int(xp)
                user_data[str(id)]["level"] = int(user_data[str(id)]["xp"] ** (1/3))
            with open("data.json", "w") as f:
                json.dump(user_data, f, indent=4)
            embed = discord.Embed(color=0x8c52ff, description=f"Increased *{user}*'s XP By {xp}")
            await ctx.send(embed = embed)
        else:
            await ctx.reply("Bruhhh! Only admins can do that")

    #Remove XP
    @commands.command()
    async def remove(self, ctx, user:discord.Member = None):
        if ctx.author.guild_permissions.administrator:
            if user is None:
                user = ctx.author
            with open("data.json", "r") as f:
                user_data = json.load(f)
            id = user.id
            await ctx.send("How many xp do you want to decrease?")
            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel
            msg = await ctx.bot.wait_for("message", check=check)
            xp = msg.content
            if str(id) in user_data:
                user_data[str(id)]["xp"] = user_data[str(id)]["xp"] - int(xp)
                user_data[str(id)]["level"] = int(user_data[str(id)]["xp"] ** (1/3))
            with open("data.json", "w") as f:
                json.dump(user_data, f, indent=4)
            embed = discord.Embed(color=0x8c52ff , description=f"Decreased *{user}*'s XP by {xp}")
            await ctx.send(embed = embed)
        else:
            await ctx.reply("Bruhhh! Only admins can do that")  

async def setup(bot):
    await bot.add_cog(admin(bot))