import hikari
import lightbulb
import pylunar
from datetime import datetime
import json
import requests
import random

plugin = lightbulb.Plugin(name="Misc")

#Command to get an 8ball answer
@plugin.command
@lightbulb.command('8ball', 'Get an 8ball answer')
@lightbulb.implements(lightbulb.SlashCommand)
async def eightball(ctx):
    answers = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", 
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.", 
        "My sources say no.", "Outlook not so good.","Very doubtful."
    ]
    await ctx.respond(random.choice(answers))


#Command to get an inspirational quote
@plugin.command
@lightbulb.command('inspire', 'Get an inspirational quote')
@lightbulb.implements(lightbulb.SlashCommand)
async def inspire(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    await ctx.respond(quote)

#Command to give the phase of the moon in Seattle
@plugin.command
@lightbulb.command('moon', 'Get the phase of the moon in Seattle')
@lightbulb.implements(lightbulb.SlashCommand)
async def moon(ctx):
    mi = pylunar.MoonInfo((47, 62, 49), (-112, 52, 10))
    mi.update(datetime.now())
    await ctx.respond('Moon Phase: ' + mi.phase_name().replace('_',' ') + f'\nPercentage: {round(mi.fractional_phase()*100,2)}%')

#Command to play a game of rock paper scissors
@plugin.command
@lightbulb.option('choice', 'rock paper or scissors', type=str)
@lightbulb.command('rps', 'Play a game of rock paper scissors')
@lightbulb.implements(lightbulb.SlashCommand)
async def rps(ctx):
    selection = ctx.options.choice.lower()
    choices = ['rock', 'paper', 'scissors']
    if selection not in choices:
        await ctx.respond('Invalid selection!')
        return
    else:
        selection = choices.index(selection)
        jester = choices[random.randint(0, 2)]
        jester = choices.index(jester)
        if selection == jester:
            await ctx.respond('Tie!\nYou: ' + choices[selection] + '\nJester: ' + choices[jester])
        elif selection == 0 and jester == 1:
            await ctx.respond('You win!\nYou: ' + choices[selection] + '\nJester: ' + choices[jester])
        elif selection == 1 and jester == 2:
            await ctx.respond('You win!\nYou: ' + choices[selection] + '\nJester: ' + choices[jester])
        elif selection == 2 and jester == 0:
            await ctx.respond('You win!\nYou: ' + choices[selection] + '\nJester: ' + choices[jester])
        else:
            await ctx.respond('You lose!\nYou: ' + choices[selection] + '\nJester: ' + choices[jester])

#Command to uwuify a string
@plugin.command
@lightbulb.option('msg', 'message to be modified', type=str)
@lightbulb.command('uwu', 'UWUify a message')
@lightbulb.implements(lightbulb.SlashCommand)
async def uwu(ctx):
    msg = ctx.options.msg
    msg = msg.replace('l', 'w')
    msg = msg.replace('r', 'w')
    msg = msg.replace('R', 'W')
    msg = msg.replace('L', 'W')
    msg = msg.replace('no', 'nyo')
    msg = msg.replace('No', 'Nyo')
    msg = msg.replace('NO', 'NYO')
    msg = msg.replace('mo', 'myo')
    msg = msg.replace('Mo', 'Myo')
    msg = msg.replace('MO', 'MYO')
    await ctx.respond(msg)

#Command to absolutely butcher a string
@plugin.command
@lightbulb.option('msg', 'message to be modified', type=str)
@lightbulb.command('why', 'turn your message into an abomination')
@lightbulb.implements(lightbulb.SlashCommand)
async def uwu(ctx):
    msg = ctx.options.msg
    msg = msg.replace('l', 'w')
    msg = msg.replace('r', 'w')
    msg = msg.replace('R', 'W')
    msg = msg.replace('L', 'W')
    msg = msg.replace('t', 'd')
    msg = msg.replace('T', 'D')
    msg = msg.replace('b', 'd')
    msg = msg.replace('B', 'D')
    msg = msg.replace('c', 'q')
    msg = msg.replace('C', 'Q')
    msg = msg.replace('e', 'æ')
    msg = msg.replace('E', 'Æ')
    msg = msg.replace('o', '0')
    msg = msg.replace('O', '0')
    msg = msg.replace('i', 'ï')
    msg = msg.replace('I', 'Ï')
    msg = msg.replace('a', 'ɐ')
    msg = msg.replace('A', 'ɐ')
    msg = msg.replace('s', 'ƨ')
    msg = msg.replace('S', 'ƨ')
    msg = msg.replace('d', 'ɗ')
    msg = msg.replace('D', 'ɗ')
    msg = msg.replace('n', 'u')
    msg = msg.replace('N', 'U')
    msg = msg.replace('m', 'ɱ')
    msg = msg.replace('M', 'ɱ')
    msg = msg.replace('w', 'ʷ')
    msg = msg.replace('W', 'ʷ')
    msg = msg.replace('v', 'ʌ')
    msg = msg.replace('V', 'ʌ')
    msg = msg.replace('p', 'ǝ')
    msg = msg.replace('P', 'ǝ')
    msg = msg.replace('y', 'j')
    msg = msg.replace('Y', 'j')
    msg = msg.replace('f', 'ƒ')
    msg = msg.replace('F', 'ƒ')
    await ctx.respond(msg)

def load(bot):
    bot.add_plugin(plugin)