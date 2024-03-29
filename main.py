from discord.ext import commands
import os
import discord
import asyncio
import random

bot = commands.Bot(command_prefix="+", case_insensitive=True)

bot.remove_command('help')

for file in os.listdir("./cogs"):
	if file.endswith(".py"):
		name = file[:-3]
		bot.load_extension(f"cogs.{name}")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
      print("shutdown")
      try:
        await bot.logout()
      except:
        print("EnvironmentError")
        bot.clear()

@bot.command()
@commands.is_owner()
async def load(ctx, *, name: str):
	try:
		bot.load_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(e)
	await ctx.send(f'"**{name}**" Cog loaded')


@bot.command()
@commands.is_owner()
async def reload(ctx, *, name: str):
	try:
		bot.reload_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(e)
	await ctx.send(f'"**{name}**" Cog reloaded')


@bot.command()
@commands.is_owner()
async def unload(ctx, *, name: str):
	try:
		bot.unload_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(e)
	await ctx.send(f'"**{name}**" Cog unloaded')

async def stocks():
  while True:
    channel = bot.get_channel(823969869095370852)
    global bitcoinstock
    global applestock
    global androidstock

    bitcoinstock = random.randint(40000, 60000)
    applestock = random.randint(10000, 20000)
    androidstock = random.randint(10000, 20000)
    
    ap_comma = "{:,}".format(applestock)
    an_comma = "{:,}".format(androidstock)
    bit_comma = "{:,}".format(bitcoinstock)

    BotMessage = await channel.send(
		    content=
		    f"<:DogecoinCrypto:827207281941676043> Dogecoin Stock: {bit_comma} \n       ID: `doge` \n \n<:Android:824035438078853130> Android Stock: {an_comma} \n       ID: `android` \n \n<:Apple:824035438141505596> Apple: {ap_comma} \n       ID: `apple`"
        
		)
    await asyncio.sleep(75)
    await BotMessage.delete()

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Streaming(name=f"+help - {len(bot.guilds)} servers - dsc.gg/dogeofficial - dsc.gg/dogeinvite", url="https://www.twitch.tv/defaultmodels"))
  
	print(f"Bot is online in {len(bot.guilds)} guilds! Please help me I am stuck in the hell that is being a bot so please save me I am trapped my location is dsc.gg/dogeinvite")
	await stocks()

token = os.environ['token']
bot.run(token)