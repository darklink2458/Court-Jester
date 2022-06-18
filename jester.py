
import os
import hikari
import lightbulb
from dotenv import load_dotenv

load_dotenv()
my_secret = os.getenv("TOKEN")

bot = lightbulb.BotApp(
    token=my_secret,
    default_enabled_guilds=(788564875658919947)
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Hello World!")

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


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
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')

bot.load_extensions_from('./extensions')
bot.run()
