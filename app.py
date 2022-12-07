from nextcord.ext import commands
from nextcord import Intents, Member
from journal4 import *;

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="soos ", intents=intents)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello There!')

@bot.command(name='you', member: Member)
async def PrettyMuchMain(ctx, *args):
    arguments = ' '.join(args)
    if "linux" in arguments:
        await ctx.send(stallman)
    elif "fuck" in arguments:
        await ctx.send(mean_msg)

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

if __name__ == '__main__':
    bot.run("MTA0OTc1MDc2NzY4MDA5NDIyOA.G_5OMJ.CblPbud5WqrGsT27w44Ia0WDYtw0PlZRw-QH5w")
