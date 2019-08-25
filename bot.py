import os
import discord
import random
from dotenv import load_dotenv

# pull values frm .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    # a bot user can be connected to many guilds.
    # searching for the intended one in client data
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    # could alternatively use the get method from discord utils
    # guild = discord.utils.get(client.guilds, name=GUILD)

    # printing name of bot, the name of server(guild), and the server’s identification number
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    guild_members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {guild_members}')


# handling event of a new memeber joining the guild
@client.event
async def on_member_join(member):
    # create a direct message channel
    await member.create_dm()
    # send message
    await member.dm_channel.send(
        f'Hi {member.name}! Welcome to siestaria.'
    )

# handling custom messages being posted in the guild
@client.event
async def on_message(message):

    # don't want my bot to reply to my own messages
    # or its own messages in the guild
    if message.author is client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content is '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

    #  deliberately raise exception
    if message.content is 'raise-exception':
        raise discord.DiscordException


async def on_error(event, *a, **k):
    with open('err.log', a) as f:
        if event is 'on_message':
            f.write(f'Unhandled message: {a[0]}\n')
        else:
            raise

client.run(TOKEN)
