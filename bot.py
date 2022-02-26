import discord

client = discord.Client()
@client.event
async def on_message(msg):
  if msg.content == "mute":
    for i in msg.author.voice.channel.members:
      await i.edit(mute=True)
    await msg.channel.send("Success Mute!")
  if msg.content == "unmute":
    for i in msg.author.voice.channel.members:
      await i.edit(mute=False)
    await msg.channel.send("Success Unmute!")
client.run(os.environ["TOKEN"])
