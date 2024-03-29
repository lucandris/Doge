import discord
from discord.ext import commands
import json
import random

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx, category=None):
      await open_account(ctx.author)
      users = await get_bank_data()
      user = ctx.author
      
      with open("mainbank.json","w") as f:
        json.dump(users,f)
        
      if category == None:
        info = "To buy an item use: buy ID", "To get more info on an item use: shop ID"
        em = discord.Embed(title = "Shop", color = discord.Color.from_rgb(47, 49, 54), description = "<:laptop:822951966975590421> **Laptop** — [2,000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `laptop` \n \n<:gun:823900537291800626> **Gun** — [5,000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \n ID: `gun` \n \n<:DogeCoin:826907590650363954> **Doge Coin** — [500,000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \nID: `coin` \n \n<:DogeMedal:826907545716392037> **Doge Medal** — [1,000,000 coins](https://www.youtube.com/watch?v=dQw4w9WgXcQ) \n ID: `medal`", inline=False)
        em.set_footer(text=f"{random.choice(info)}")

        await ctx.send(embed = em)
        return

      if category == "medal":
        medal_amt = users[str(user.id)]["medal"]
        em = discord.Embed(title = f"Doge Medal ({medal_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Used to mega flex on poor players. That's it.")
        em.add_field(name="Value:", value="Buy: 1,000,000 coins \nSell: Not sellable")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/826907664335241216/Untitled_design__2_-removebg-preview.png")

        await ctx.send(embed = em)
        return

      if category == "coin":
        medal_amt = users[str(user.id)]["coin"]
        em = discord.Embed(title = f"Doge Coin ({medal_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Used to flex on poor players. That's it.")
        em.add_field(name="Value:", value="Buy: 500,000 coins \nSell: Not sellable")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/826907667909967892/Untitled_design__3_-removebg-preview.png")

        await ctx.send(embed = em)
        return

      if category == "laptop":
        laptop_amt = users[str(user.id)]["laptop"]
        em = discord.Embed(title = f"Laptop ({laptop_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Allows you to postmemes on reddit for coins. ```+postmemes```")
        em.add_field(name="Value:", value="Buy: 2000 coins \nSell: 1000 coins")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823539841089404988/1447_laptop.png")

        await ctx.send(embed = em)
        return

      if category == "gun":
        gun_amt = users[str(user.id)]["gun"]
        em = discord.Embed(title = f"Gun ({gun_amt} owned)",color = discord.Color.from_rgb(47, 49, 54),description = "Allows you to rob other players of their wallets. ```+rob MENTION```")
        em.add_field(name="Value:", value="Buy: 5000 coins \nSell: 2500")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/796440127857229855/823900235649777684/1426_pistol.png")

        await ctx.send(embed = em)
        return
    

async def open_account(user):
  
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 250
    users[str(user.id)]["multi"] = 2
    users[str(user.id)]["bank"] = 0
    users[str(user.id)]["bankmax"] = 100
    users[str(user.id)]["laptop"] = 0
    users[str(user.id)]["premium"] = 0 
    users[str(user.id)]["gun"] = 0 
    users[str(user.id)]["btc"] = 0 
    users[str(user.id)]["apple"] = 0     
    users[str(user.id)]["android"] = 0
    users[str(user.id)]["medal"] = 0
    users[str(user.id)]["coin"] = 0
 
    

  with open("mainbank.json","w") as f:
    json.dump(users,f)
  return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
      users = json.load(f)

    return users


async def update_bank(user,change = 0,mode = "wallet"):
  users = await get_bank_data()
  
  users[str(user.id)][mode] += change

  with open("mainbank.json","w") as f:
    json.dump(users,f)
  return True

def setup(bot):
    bot.add_cog(Shop(bot))
