#pip install discord
import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(' https://discord.gg/VUdGVfRvCY') #Message
      print(f"Messaged {user.name}")
    except:
       print(f"Couldn't message {user.name}")

client.run('tokengoeshere', bot=False) #User Token