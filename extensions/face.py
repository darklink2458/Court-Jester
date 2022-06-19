import hikari
import lightbulb
import requests

plugin = lightbulb.Plugin(name="Misc")

#Command to get a face from thispersondoesnotexist.com
@plugin.command
@lightbulb.command('face', 'Get a random face from thispersondoesnotexist.com')
@lightbulb.implements(lightbulb.SlashCommand)
async def face(ctx):
    response = requests.get("https://thispersondoesnotexist.com/image")
    file = open("img.jpg", 'wb')
    file.write(response.content)
    file.close()
    f = hikari.File('img.jpg')
    await ctx.respond(f)

def load(bot):
    bot.add_plugin(plugin)