import discord
from discord.ext import commands

class helpBox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name='help', invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
            title = '<Help Menu/>', color=0x8c52ff)
        em.add_field(name="General", value="`>rank` `>leaderboard` `>ping`")
        em.add_field(name="Admin", value="`>add` `>remove`")
        em.set_image(url="https://media.discordapp.net/attachments/870649335451361320/870944688545366057/Narrow_rgb_loading.gif")
        em.set_footer(text = f"@{ctx.author} For detailed help use >help <command>")
        await ctx.send(embed=em)

    @help.command(name='rank')
    async def rank(self, ctx):
        em = discord.Embed(title = '<Help Menu/>', description="""
`>rank` - Shows you your Rank and XP
Aliases: `>r`
    """, color=0x8c52ff)
        em.set_footer(text = f"Requested by @{ctx.author}")
        em. set_image(url="https://media.discordapp.net/attachments/870649335451361320/870944688545366057/Narrow_rgb_loading.gif")
        await ctx.send(embed=em)

    @help.command(name='leaderboard', aliases=['lb', 'top'])
    async def leaderboard(self, ctx):
        em = discord.Embed(title = '<Help Menu/>', description="""
`>leaderboard` - Displays the all time Leaderboard
Aliases: `>lb`, `>top`
    """, color=0x8c52ff)
        em.set_footer(text = f"Requested by @{ctx.author}")
        em. set_image(url="https://media.discordapp.net/attachments/870649335451361320/870944688545366057/Narrow_rgb_loading.gif")
        await ctx.send(embed=em)
    
    @help.command(name='ping')
    async def ping(self, ctx):
        em = discord.Embed(title = '<Help Menu/>', description="""
`>ping` - Displays the latency of the bot
Aliases: None
    """, color=0x8c52ff)
        em.set_footer(text = f"Requested by @{ctx.author}")
        em. set_image(url="https://media.discordapp.net/attachments/870649335451361320/870944688545366057/Narrow_rgb_loading.gif")
        await ctx.send(embed=em)

    @help.command(name='add')
    async def add(self, ctx):
        em = discord.Embed(title = '<Help Menu/>', description="""
`>add` - Admins can add XP to any user
Aliases: None
    """, color=0x8c52ff)
        em.set_footer(text = f"Requested by @{ctx.author}")
        em. set_image(url="https://media.discordapp.net/attachments/870649335451361320/870944688545366057/Narrow_rgb_loading.gif")
        await ctx.send(embed=em)

    @help.command(name='remove')
    async def remove(self, ctx):
        em = discord.Embed(title = '<Help Menu/>', description="""
`>remove` - Admins can decrease XP from any user
Aliases: None
    """, color=0x8c52ff)
        em.set_footer(text = f"Requested by @{ctx.author}")
        em. set_image(url="https://media.discordapp.net/attachments/870649335451361320/870944688545366057/Narrow_rgb_loading.gif")
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(helpBox(bot))
