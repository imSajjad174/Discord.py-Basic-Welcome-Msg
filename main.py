import discord
from discord.ext import commands

intents = discord.Intents.default()  # Create an instance of the default Intents class
intents.typing = False  # Disable typing events for better performance
intents.presences = False  # Disable presence events for better performance


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')




@bot.command()
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f'The result is {result}')







@bot.event
async def on_member_join(member):
    # Customize your welcome message here
    welcome_message = f"Welcome {member.mention} to the server! Enjoy your stay."

    # Find the channel where you want to send the welcome message
    channel = discord.utils.get(member.guild.text_channels, name='welcome')

    if channel:
        await channel.send(welcome_message)









bot.run('TOKEN')
