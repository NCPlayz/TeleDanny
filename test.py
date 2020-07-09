from framework import Bot, Context

from config import token, owners

bot = Bot(token=token, owners=owners)

@bot.command()
def test_case(ctx: Context):
    ctx.reply('no u')

@bot.command()
def test_case_2(ctx: Context):
    ctx.send('<b>haha yes</b>', html=True)

@bot.command(owner_only=True)
def eval(ctx: Context):
    ctx.send('super secret data shh')

@bot.command(owner_only=True)
def add_owner(ctx: Context):
    bot.owners.append(int(ctx.args[0]))
    ctx.send('added to owner list.')

bot.run()
