from discord.ext import commands
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


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
