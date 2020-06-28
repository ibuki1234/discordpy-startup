from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'おい槇原':
        await message.channel.send('もうシャブなんてしないなんて言わないよ絶対')  
        await message.channel.send('https://nikkan-spa.jp/wp-content/uploads/2017/12/yakubutsu2017-550x357.jpg')

client.run('Njk2MzI2MzE0MDg0MjcwMTEw.Xvgj0g.rQ2KnHDOSXUYjcHnLvKEeutvKgc')
