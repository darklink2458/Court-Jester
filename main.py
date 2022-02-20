import os
import hikari
import lightbulb
#my_secret = os.environ['TOKEN']

#bot = lightbulb.BotApp(token=my_secret)
bot = lightbulb.BotApp(token="OTQ0ODQwMDk3OTQ4MzkzNTAy.YhHc6Q.0LZoNE3Ds0f26f_r_CUahydW0mo")

@bot.listen(hikari.GuildMessageCreateEvent)
async def ping(event) -> None:
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get `None' here.
    if event.is_bot or not event.content:
        return

    if event.content.startswith("hk.ping"):
        await event.message.respond("Pong!")

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('The Jester Has Arrived!')

bot.run()
