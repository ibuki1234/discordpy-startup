import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'おい槇原':
        await message.channel.send('もうシャブなんてしないなんて言わないよ絶対')  
        await message.channel.send('https://nikkan-spa.jp/wp-content/uploads/2017/12/yakubutsu2017-550x357.jpg')




bot.run(token)
