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
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    # printing name of bot, the name of server(guild), and the server’s identification number
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    guildMembers = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {guildMembers}')

client.run(TOKEN)
