import os
import discord
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
    # guild = discord.utils.get(client.guilds, name=GUILD)

    # printing name of bot, the name of server(guild), and the server’s identification number
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    guild_members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {guild_members}')


@client.event
async def on_member_join(member):
    # create a direct message channel
    await member.create_dm()
    # send message
    await member.dm_channel.send(
        f'Hi {member.name}! Welcome to siestaria.'
    )

client.run(TOKEN)
