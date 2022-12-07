from nextcord.ext import commands
from nextcord import Intents
from journal4 import *;

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents)

async def mainboi(ctx, arguments):
    if "linux" in arguments:
        await ctx.send(stallman)
    elif "fuck" in arguments:
        await ctx.send(mean_msg)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello There!')

@bot.command(name='a')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)

@bot.command(name='b')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='c')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='d')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='e')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='f')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='g')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='h')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='i')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='j')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='k')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='l')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='m')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='n')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='o')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='p')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='q')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='r')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='s')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='t')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='u')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='v')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='w')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='x')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='y')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)
@bot.command(name='z')
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    await mainboi(ctx, arguments)



@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

if __name__ == '__main__':
    bot.run("MTA0OTc1MDc2NzY4MDA5NDIyOA.G_5OMJ.CblPbud5WqrGsT27w44Ia0WDYtw0PlZRw-QH5w")
