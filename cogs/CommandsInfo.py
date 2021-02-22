import discord
from discord.ext import commands

class CommandsInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, category=None):
      if category == None:
        em = discord.Embed(title = "Help",color = discord.Color.from_rgb(47, 49, 54))
        em.add_field(name = "Currency",value = "```cook, beg, farm, balance,  work, postmemes, search, slots, multiplier, prestige```", inline=False)
        em.add_field(name = "Fun",value = "```roast, pp, 8ball, fact, gayrate, dograte, showerthoughts, thotrate, dogerate, meme```", inline=False)
        em.add_field(name = "Other",value = "```ping```", inline=False)
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "work":
        em = discord.Embed(title = "Work command",color = discord.Color.from_rgb(47, 49, 54),description = "Work and earn coins. ```+work```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "thotrate":
        em = discord.Embed(title = "Thotrate command",color = discord.Color.from_rgb(47, 49, 54),description = "Informs you of the percent of thot in your body. ```+thotrate```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "slots":
        em = discord.Embed(title = "Slots command",color = discord.Color.from_rgb(47, 49, 54),description = "Don't gamble kids!. ```+slots```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "showerthoughts":
        em = discord.Embed(title = "Showerthougts command",color = discord.Color.from_rgb(47, 49, 54),description = "Sends things people only think of in the shower. ```+showerthoughts```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return
    
      if category == "search":
        em = discord.Embed(title = "Search command",color = discord.Color.from_rgb(47, 49, 54),description = "Search an area for coins (You can die). ```+search```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "roast":
        em = discord.Embed(title = "Roast command",color = discord.Color.from_rgb(47, 49, 54),description = "Get roasted by the bot. ```+roast```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "prestige":
        em = discord.Embed(title = "Prestige command",color = discord.Color.from_rgb(47, 49, 54),description = "Spend 25k and get 1-5 multipliers added. ```+prestige```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "pp":
        em = discord.Embed(title = "PP command",color = discord.Color.from_rgb(47, 49, 54),description = "Check your PP size. ```+pp```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "postmemes":
        em = discord.Embed(title = "Postmemes command",color = discord.Color.from_rgb(47, 49, 54),description = "Post memes on reddit for ad money. ```+postmemes```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "ping":
        em = discord.Embed(title = "Ping command",color = discord.Color.from_rgb(47, 49, 54),description = "Check the bot's delay to discord servers. ```+ping```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "multiplier":
        em = discord.Embed(title = "Multiplier command",color = discord.Color.from_rgb(47, 49, 54),description = "Check your current multiplier. ```+multiplier```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "gayrate":
        em = discord.Embed(title = "Gayrate command",color = discord.Color.from_rgb(47, 49, 54),description = "Informs you of the percent of gayness in your body. ᴰᶦˢᶜˡᵃᶦᵐᵉʳ ᵀʰᶦˢ ᶦˢ ᵒⁿˡʸ ᵃ ᵐᵉᵐᵉ ᵃⁿᵈ ᴵ ʰᵃᵛᵉ ⁿᵒᵗʰᶦⁿᵍ ᵃᵍᵃᶦⁿˢᵗ ᵍᵃʸ ᵖᵉᵒᵖˡᵉ ```+gayrate```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "farm":
        em = discord.Embed(title = "Farm command",color = discord.Color.from_rgb(47, 49, 54),description = "Farm and sell your production for coins. ```+farm```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "fact":
        em = discord.Embed(title = "Fact command",color = discord.Color.from_rgb(47, 49, 54),description = "Sends a random fact. ```+fact```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "dograte":
        em = discord.Embed(title = "Dograte command",color = discord.Color.from_rgb(47, 49, 54),description = "Informs you of the percent of dog in your body. ```+dograte```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "dogerate":
        em = discord.Embed(title = "Dogerate command",color = discord.Color.from_rgb(47, 49, 54),description = "Informs you of the percent of doge in your body. ```+dogerate```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "cook":
        em = discord.Embed(title = "Cook command",color = discord.Color.from_rgb(47, 49, 54),description = "Cook some cookies :cookie: and sell them. ```+cook```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return

      if category == "beg":
        em = discord.Embed(title = "Beg command",color = discord.Color.from_rgb(47, 49, 54),description = "Beg for money, See how nice people are. ```+beg```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)

      if category == "8ball":
        em = discord.Embed(title = "8ball command",color = discord.Color.from_rgb(47, 49, 54),description = "Ask a question to the 8ball and get an answer. ```+8ball YOUR_QUESTION```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return
    
      if category == "balance":
        em = discord.Embed(title = "Balance command",color = discord.Color.from_rgb(47, 49, 54),description = "Tells you how much money you have. ```+balance```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return
      
      if category == "meme":
        em = discord.Embed(title = "Meme command",color = discord.Color.from_rgb(47, 49, 54),description = "Get some fresh memes straight out of reddit. ```+meme```")
        em.add_field(name=":link: Quick Links",value="[Vote For Me](https://top.gg/bot/785160383560286240/vote) - [Invite Me](https://discord.com/oauth2/authorize?client_id=785160383560286240&scope=bot&permissions=2147483647) - [Support Server](https://discord.gg/3d6BpRHvbR) - [Premium/Donate](https://donatebot.io/checkout/794412631543906365)", inline=False)
        await ctx.send(embed = em)
        return        
       
def setup(bot):
    bot.add_cog(CommandsInfo(bot))
