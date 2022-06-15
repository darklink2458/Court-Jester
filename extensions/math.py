import hikari
import lightbulb

plugin = lightbulb.Plugin(name="Math")

@plugin.command
@lightbulb.command('math_commands', 'Group of math commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def math_commands(ctx):
    pass

#Command to add a number two numbers
@math_commands.child
@plugin.command
@lightbulb.option('y', 'The second number', type=float)
@lightbulb.option('x', 'The first number', type=float)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def add(ctx):
    await ctx.respond(ctx.options.x + ctx.options.y)

#Command to subtract a number from another number
@math_commands.child
@plugin.command
@lightbulb.option('y', 'The second number', type=float)
@lightbulb.option('x', 'The first number', type=float)
@lightbulb.command('subtract', 'Subtract a number from another number')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subtract(ctx):
    await ctx.respond(ctx.options.x - ctx.options.y)

#Command to multiply two numbers together
@math_commands.child
@plugin.command
@lightbulb.option('y', 'The second number', type=float)
@lightbulb.option('x', 'The first number', type=float)
@lightbulb.command('multiply', 'Multiply two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multiply(ctx):
    await ctx.respond(ctx.options.x * ctx.options.y)

#Command to divide two numbers together
@math_commands.child
@plugin.command
@lightbulb.option('y', 'The second number', type=float)
@lightbulb.option('x', 'The first number', type=float)
@lightbulb.command('divide', 'Divide two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def divide(ctx):
    await ctx.respond(ctx.options.x / ctx.options.y)

#Command to square a number
@math_commands.child
@plugin.command
@lightbulb.option('x', 'The number to square', type=float)
@lightbulb.command('square', 'Square a number')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def square(ctx):
    await ctx.respond(ctx.options.x ** 2)

#Command to square root a number
@math_commands.child
@plugin.command
@lightbulb.option('x', 'The number to square root', type=float)
@lightbulb.command('square_root', 'Square root a number')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def square_root(ctx):
    await ctx.respond(ctx.options.x ** 0.5)



def load(bot):
    bot.add_plugin(plugin)