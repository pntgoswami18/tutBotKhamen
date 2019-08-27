import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

# pull values frm .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    """Triggered when the bot is connected and ready
    """
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
    """Handles new members joining

    Arguments:
        member {object} -- Discord memeber object
    """
    # create a direct message channel
    await member.create_dm()
    # send message
    await member.dm_channel.send(
        f'Hi {member.name}! Welcome to siestaria.'
    )

# handling custom messages being posted in the guild
@client.event
async def on_message(message):
    """Handler for message event triggers

    Arguments:
        message {string} -- Message trigger

    Raises:
        exception: Exception on unhandled events
        discord.DiscordException: Discord exception raised
    """

    # don't want my bot to reply to my own messages
    # or its own messages in the guild
    print(f'author is {message.author}')
    print(f'message is {message.content}')
    if message.author == client.user:
        return

    # To-Do: move these texts into files and read from there
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Sarge, with all due respect, I am gonna completely ignore everything you just said.💁‍',
        '''The English language can not fully capture the depth and complexity of my thoughts, 
        so I’m incorporating emojis into my speech to better express myself. 😉''',
        'A place where everybody knows your name is hell. You’re describing hell.',
        'If I die, turn my tweets into a book.',
        'I asked them if they wanted to embarrass you, and they instantly said yes.',
        'Great, I’d like your $8-est bottle of wine, please.',
        'Captain Wuntch. Good to see you. But if you’re here, who’s guarding Hades?',
        'I’m playing Kwazy Cupcakes, I’m hydrated as hell, and I’m listening to Sheryl Crow. I’ve got my own party going on.',
        'Anyone over the age of six celebrating a birthday should go to hell.',
        'Captain, turn your greatest weakness into your greatest strength. Like Paris Hilton RE: her sex tape.',
        'Jake, piece of advice: just give up. It’s the Boyle way. It’s why our family crest is a white flag.'
    ]

    hindi_expletives_triggers = [
        'bc', 'bencho', 'mc', 'madarchod', 'bsdk', 'bhosdike'
    ]

    # add some flavor here
    hindi_expletives = [
        'mera lawda',
        'bde hi ajeeb chutiye ho yaar tum',
        'gaand m chattri daal k khol dunga aage bola to',
        'ha tera baap hai, gandu',
        'chup madarchod!',
        'chup kar bhosdike',
        'aisa marunga, parle-g kaali chai m dubona b naseeb nhi hoga',
        'kya bawaseer hai re ye?!',
        'gaali kaun diya bc?!'
    ]

    saanp_replies = [
        'abu hai asli saanp mc',
        'insaan hi insaan ko dass raha hai, saanp side m baith k hass raha h',
        'ye jo saath m haste hain, baad m saanp ban k daste hain :snake:',
    ]

    welcome_salutations = [
        'hi', 'hello', 'how are you', 'hey'
    ]

    welcome_replies = [
        f'kaun laya is {message.author} ko?!',
        f'aao {message.author}. Guruji ka prasad leke jaoge.',
        f'aham brahmasmi',
    ]

    if message.content == '99!':
        print('99! triggered')
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if 'happy birthday' in message.content.lower():
        print('HDB triggered')
        await message.channel.send('Happy Birthday! 🎈🎉')

    #  deliberately raise exception
    if message.content == 'raise-exception':
        raise discord.DiscordException

    if 'sun be' in message.content.lower():
        await message.channel.send('chup madarchod! bilkul chup!')

    if 'ssup' in message.content.lower():
        await message.channel.send('bol bhadwe, teri baari ab')

    if 'saanp' in message.content.lower():
        response = random.choice(saanp_replies)
        await message.channel.send(response)

    if 'koi' in message.content.lower():
        await message.channel.send('ha tera baap hai, gandu')

    if 'kaun' in message.content.lower():
        await message.channel.send('register m dekh insaan h ya bhagwaan')

    for x in hindi_expletives_triggers:
        if x in message.content.lower():
            response = random.choice(hindi_expletives)
            await message.channel.send(response)

    # random replies to welcome salutions
    for x in welcome_salutations:
        if x in message.content.lower():
            response = random.choice(welcome_replies)
            await message.channel.send(response)

    # randomly send messages when abu messages
    if str(message.author) == 'abutaha#2650':
        send_message = random.choice([True, False])
        if (send_message):
            response = random.choice(hindi_expletives)
            await message.channel.send(response)


# error handler
async def on_error(event, *a, **k):
    """Error handler and logger for on_message raised errors

    Arguments:
        event {object} -- Event for which the exception is raised
    """
    with open('err.log', a) as f:
        if event is 'on_message':
            f.write(f'Unhandled message: {a[0]}\n')
        else:
            raise discord.DiscordException

client.run(TOKEN)
