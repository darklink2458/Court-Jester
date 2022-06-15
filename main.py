import os
import hikari
import lightbulb
#my_secret = os.environ['TOKEN']

#bot = lightbulb.BotApp(token=my_secret)
bot = lightbulb.BotApp(
    token="OTQ0ODQwMDk3OTQ4MzkzNTAy.YhHc6Q.0LZoNE3Ds0f26f_r_CUahydW0mo",
    default_enabled_guilds=(788564875658919947)
)

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

@bot.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("foo", "test command")
@lightbulb.implements(lightbulb.SlashCommand)
async def foo(ctx):
    await ctx.respond("You are the owner of this bot.")

@bot.command
@lightbulb.command('my_group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')

bot.run()
