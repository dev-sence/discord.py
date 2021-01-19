import discord
from discord.ext import commands, tasks

bot = commands.Bot (command_prefix="!")

token = "토큰"

@bot.event
async def on_ready():
    print("Bot Connected")
    print(f"Bot name: {bot.user.name}")
    print(f"ID: {bot.user.id}")
  
@bot.command()
async def ping(ctx):
    await ctx.send(":ping_pong:  Pong!")
  
bot.run(token)
