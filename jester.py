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
    print("Bot is online!")


@bot.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("foo", "test command")
@lightbulb.implements(lightbulb.SlashCommand)
async def foo(ctx):
    await ctx.respond("You are the owner of this bot.")
    

@bot.command
@lightbulb.command('information', 'Basic information about the bot and its author')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def info_group(ctx):
    pass

#Command that says hello to Jester's author
@info_group.child
@lightbulb.command('owner', "Pings Jester's owner")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('Hi <@271347480291966977>!')

#Command that links to Jester's GitHub Repository
@info_group.child
@lightbulb.command('github', "Links to Jester's GitHub Repository")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('https://github.com/darklink2458/Court-Jester')

#Command that sends a ping to Jester
@info_group.child
@lightbulb.command('ping', 'pings Jester')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


bot.load_extensions_from('./extensions')
bot.run()
