import os
import json
import time
from fivem import FiveM
import discord
from discord.ext import commands, tasks

# Discord bot setup, you can ignore these.
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.messages = True  # Enable privileged message content intent
intents.guilds = True  # Enable privileged guilds intent
bot = commands.Bot(command_prefix='!', intents=intents)

# You need to configure all these to fit your specifications.
bot_token = "" # Type your Discord Bot token here.
join_leave_channel_id = 1234567890 # Type the channel ID on Discord where you want it to output the join/leave messages. You find this by Enabling Discord Developer Mode and right-clicking a channel and Copy ID.
allowed_user_ids = ['1237', '2345', '2347'] # Discord User IDs that are allowed to use the !playerlist command.
ip = "123.123.123.123" # IP of the FiveM Server
port = 30120 # Port of FiveM server. Default is 30120

# Command to generate a coupon
@bot.command()
async def playerlist(ctx):
    user_id = str(ctx.author.id)
    if user_id in allowed_user_ids:
        players = await fivem_player_list()
        # Join the player names with a newline character to form a single string
        message = "\n".join(players)
        await ctx.send(f"Current online players:\n{message}")
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

#A task that checks the server list every minute, can increase/decrease this as needed.
@tasks.loop(minutes=1)
async def fivem_join_leave():
    print("Checking online players...") # Debugging, you can remove this line.
    status_file = 'current_players.json'
    new_players = await fivem_player_list()
    current_time = time.time()

    # Load the old status from the file
    with open(status_file, 'r') as file:
        if file.read().strip():
            file.seek(0)  # reset file pointer to beginning
            old_status = json.load(file)
        else:
            old_status = {}

    for player in new_players:
        # If the player is not in the old status, they have just joined
        if player not in old_status:
            old_status[player] = current_time
            try:
                await bot.get_channel(discord_channel_id).send(f":green_square:  ``{player}``")
            except Exception as e:
                print(f"Error sending message: {e}")

    for player, join_time in list(old_status.items()):
        if player not in new_players:
            # The player has left
            duration = current_time - join_time
            hours, remainder = divmod(duration, 3600)
            minutes, _ = divmod(remainder, 60)
            try:
                await bot.get_channel(discord_channel_id).send(f":red_square: ``{player}`` (Online for {int(hours)} hours and {int(minutes)} minutes)")
                del old_status[player]
            except Exception as e:
                print(f"Error sending message: {e}")

    # Save the new status to the file
    with open(status_file, 'w') as file:
        json.dump(old_status, file)

async def fivem_player_list():
    fivem = FiveM(ip=ip, port=port)

    players = await fivem.get_players()
    # Extract and sort the player names
    player_names = sorted([player.name for player in players])
    return player_names

@bot.event
async def on_ready():
    print("Bot is ready.")
    fivem_join_leave.start()

# Check if the file exists and is not empty
status_file = 'current_players.json'
if not os.path.isfile(status_file) or os.stat(status_file).st_size == 0:
    with open(status_file, 'w') as file:
        json.dump({}, file)

bot.run(bot_token)
