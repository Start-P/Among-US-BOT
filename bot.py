import discord
import ffmpeg #replitで実行するため、オートインポートに引っかかるようにする。 import os -> os.system("pip install ffmpeg") でも良い
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
  if msg.content.startwith("!play"):
    voice = await msg.author.voice.channel.connect() #vcに接続
    music = await voice.create_ytdl_player(msg.content.split(" ")[1]) #空白でsplitしてurlを抽出
    music.start()
client.run(os.environ["TOKEN"])
