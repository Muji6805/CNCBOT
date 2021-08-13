import discord
from discord.ext import commands

TOKEN = "my tooooooooooken :p"
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} online!")
    game = discord.Game("")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("https://discord.gg"):
        if message.guild:
            if message.author.guild_permissions.manage_messages: 
                print("관리자니깐 스킵")
            else:
                await message.delete()
                await message.channel.send("디스코드 서버 홍보하시면 안됩니다")
        else:
            await message.channel.send("DM으로는 불가능합니다")

client.run(TOKEN)
