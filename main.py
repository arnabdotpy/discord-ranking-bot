import json
from discord.ext import commands, tasks
from datetime import time
import time
import discord
import operator
import os

vcList = [] #VC IDs of VC's where you want this bot to add rank
prefix = ">"

bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())
bot.remove_command('help')

#***************COGS***************
async def load_cogs(bot):
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def unload_cogs(bot):
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            await bot.unload_extension(f'cogs.{file[:-3]}')

@bot.command()
async def reload(ctx):
    if not ctx.author.id in []: #Add ID's of people who can reload cogs 
        await ctx.send("Only veriied people can reload cogs...")
        return
    await ctx.send("Unloading Cogs")
    await unload_cogs(bot)
    await ctx.send("Cogs Unloaded, Reloading Cogs...")
    await load_cogs(bot)
    await ctx.send("Cogs Reloaded")

#*************ON READY*************
@bot.event
async def on_ready():
    activity = discord.Game(name="Push To Prod")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print('---> Logged in as {0.user}'.format(bot))
    #await bot.add_cog(ranking(bot))
    await load_cogs(bot)
    print("---> Cogs Loaded")

#***************CHAT POINTS***************
@bot.event
async def on_message(member):
    with open("data.json", "r") as f:   
        user = json.load(f)
    id = member.author.id
    if  member.content.startswith(prefix) or member.author.bot is True or member.guild is None:
        await bot.process_commands(member)
    elif str(id) not in user:
        user[str(id)] = {}
        user[str(id)]['xp'] = 0
        user[str(id)]['level'] = 1
        with open("data.json", "w") as f: 
            json.dump(user, f, indent=4)
        await bot.process_commands(member)
    else:
        if str(id) in user:
            user[str(id)]["xp"] += 3
            user[str(id)]["level"] = int(user[str(id)]["xp"] ** (1/3))
            new_level = user[str(id)]["level"]
        with open("data.json", "w") as f: 
            json.dump(user, f, indent=4)

#***************POINTS ON VC***************
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel.id in vcList:
        with open("data.json", "r") as f:   
            user = json.load(f)     
        id = member.id
        if str(id) in user: 
            if before.channel is None and after.channel is not None: 
                join_time = time.time()
                id = member.id
                with open("time_data.json","r") as f:
                    user = json.load(f)
                    user[str(id)] = int(join_time)
                with open("time_data.json","w") as f:
                    json.dump(user, f, indent=4)   
                channel = bot.get_channel(1014511314103697458)
    elif before.channel is not None and before.channel.id in vcList: 
        if before.channel is not None and after.channel is None:
            leave_time = time.time()
            id = member.id
            with open("time_data.json","r") as f:
                user = json.load(f)
                initial = user[str(id)]
                time_spent = int(leave_time) - int(initial)
                points = int(time_spent/60)
                with open("data.json","r") as f:
                    file = json.load(f)
                    file[str(id)]["xp"] += points
                    file[str(id)]["level"] = int(file[str(id)]["xp"] ** (1/3))
                with open("data.json", "w") as f:
                    json.dump(file, f, indent=4)
                channel = bot.get_channel(1014511314103697458)
                await channel.send(f"```{member} spent {time_spent}s in VC | {points}XP Added```")   
                
bot.run("TOKEN") #Bot token here
