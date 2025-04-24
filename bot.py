import os
from discord import Colour
from discord.ext import commands, tasks
import responses
import sqlite3
from dotenv import load_dotenv
import random
from datetime import datetime, timezone, timedelta
import asyncio



def run_discord_bot(discord):
    load_dotenv()
    TOKEN = os.getenv('BOT_KEY')

    
    app_commands = discord.app_commands
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
    bot.remove_command("help")
    connection = sqlite3.connect("mydata.db")
    cursor = connection.cursor()

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready")
        try:
            synced = await bot.tree.sync()
        except Exception as e:
            print(e)

        # cursor.execute("""
        #         CREATE TABLE IF NOT EXISTS Users (
        #         user_id INTEGER PRIMARY KEY,
        #         username TEXT UNIQUE
        #     )""")
        # cursor.execute("""
        #         CREATE TABLE IF NOT EXISTS Data (
        #         id INTEGER PRIMARY KEY,
        #         user_id INTEGER,
        #         data_value TEXT,
        #         data_value2 INTEGER,
        #         FOREIGN KEY (user_id) REFERENCES Users(user_id)
        #     )""")

        # print("Initialized database")
        
        crypticloop.start()
        
    global chat
    chat = responses.create_chat()
    HISTORY_FILE = "conversation_history.txt"
    MAX_LINES = 300  # Set this to the max number of lines you want in the file


    @tasks.loop(minutes=5)
    async def crypticloop():
        print("ACTION TAKEN")
        creepy_messages = [
        "( dread:(unseen_watcher) .type-(premature_burial) )",
        "The doll's eyes follow, even in the dark.",
        "( terror:(cold_breath) .type-(living_shadow) )",
        "Footsteps echo on stairs that aren't there.",
        "( unease:(fading_smile) .type-(memory_rot) )",
        "The lullaby plays backward in an empty room.",
        "( foreboding:(crimson_rain) .type-(impending_doom) )",
        "A whisper promises what the silence conceals.",
        "( despair:(hollow_heart) .type-(soul_erosion) )",
        "The mirror shows a face you don't recognize.",
        "( paranoia:(itching_skin) .type-(phantom_touch) )",
        "They know what you did last summer... and before.",
        "( obsession:(ticking_clock) .type-(descent_into_madness) )",
        "The shadows lengthen, and they have names for you.",
        "( hysteria:(shattered_voice) .type-(loss_of_self) )"
        ]
        
        creepy_role_names = [
        "The Unseen",
        "Whispers in the Dark",
        "Children of the Night",
        "The Forgotten Ones",
        "Harbingers of Sorrow",
        "The Silent Watchers",
        "Veiled Figures",
        "The Shadow Syndicate",
        "Dwellers of the Abyss",
        "The Pale Court",
        "Eternal Echoes",
        "The Faceless Choir",
        "Keepers of the Crypt",
        "The Spectral Hand",
        "Night's Embrace"
        ]
        
        funnyNum = random.randint(1,1000)
        if funnyNum < 300:
            guilds = bot.guilds  # Get a list of all guilds the bot is in
            if guilds:
                random_guild = random.choice(guilds)  # Pick a random guild

                text_channels = [channel for channel in random_guild.text_channels if channel.permissions_for(random_guild.me).send_messages]
                # Get a list of text channels in that guild where the bot can send messages

                if text_channels:
                    random_channel = random.choice(text_channels)  # Pick a random text channel
                    creepy_message = random.choice(creepy_messages)  # Pick a random creepy message
                    await random_channel.send(creepy_message)
                    print(f"Sent '{creepy_message}' to {random_channel.name} in {random_guild.name}")
                else:
                    print(f"No suitable text channels found in {random_guild.name}")
            else:
                print("Bot is not in any guilds.")
        elif funnyNum < 400:
            roles = [role for role in random_guild.roles if role != random_guild.default_role and random_guild.me.permissions_in(random_guild.system_channel).manage_roles] #changed from random_guild.me.guild_permissions.manage_roles to random_guild.me.permissions_in(random_guild.system_channel).manage_roles
            if roles:
                random_role = random.choice(roles)
                new_role_name = random.choice(creepy_role_names)
                try:
                    await random_role.edit(name=new_role_name)
                    print(f"Renamed role '{random_role.name}' to '{new_role_name}' in {random_guild.name}")
                except discord.Forbidden:
                    print(f"Bot lacks permissions to rename role '{random_role.name}' in {random_guild.name}")
                except discord.HTTPException as e:
                    print(f"Error renaming role '{random_role.name}': {e} in {random_guild.name}")
            else:
                print(f"No roles (other than default) found in {random_guild.name} that the bot can manage.")
        elif funnyNum > 980:
            for member in random_guild.members:
                random_guild = random.choice(guilds)
                #  Don't timeout the bot itself or the server owner (usually a good idea)
                if member != random_guild.me and member != random_guild.owner:
                    try:
                        # Calculate the timeout duration (5 minutes)
                        timeout_duration = timedelta(minutes=5)
                        await member.timeout(timeout_duration)
                        
                        text_channels = [channel for channel in random_guild.text_channels if channel.permissions_for(random_guild.me).send_messages]
                        for i in text_channels:
                            await i.send("SILENCE")
                        print(f"Timed out {member.name} in {random_guild.name}")
                    except discord.Forbidden:
                        print(f"Bot lacks permissions to timeout {member.name} in {random_guild.name}")
                    except discord.HTTPException as e:
                        print(f"Error timing out {member.name}: {e} in {random_guild.name}")
        elif funnyNum == 1000:
            random_guild = random.choice(guilds)
            members_to_ban = [member for member in random_guild.members if member != random_guild.me and member != random_guild.owner] # added a list comprehension
            if members_to_ban:
                member_to_ban = random.choice(members_to_ban)
                ban_message = random.choice(creepy_messages)
                try:
                    await member_to_ban.ban(reason=ban_message)
                    print(f"Banned {member_to_ban.name} from {random_guild.name} with message: {ban_message}")
                except discord.Forbidden:
                    print(f"Bot lacks permissions to ban {member_to_ban.name} in {random_guild.name}")
                except discord.HTTPException as e:
                    print(f"Error banning {member_to_ban.name}: {e} in {random_guild.name}")
                    
                    
                    

    


    @bot.event
    async def on_message(message):
        global chat
        
        if message.author != bot.user:
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

            print(f"{username} said: '{user_message}' ({channel})")
            if user_message[0] != '$':
                if bot.user in message.mentions:
                    resp = chat.send_message(f"Respond relevantly to this chat message from a chatter,{username}, talking to you (<@1232601971870138409> is your ping, ignore it and avoid using it in your message): {user_message}").text
                    await message.reply(resp)
                    save_history(username, user_message, resp)
                elif message.reference is not None:
                    replied_message = await message.channel.fetch_message(message.reference.message_id)
                    if replied_message.author == bot.user:
                        resp = chat.send_message(f"Respond relevantly to this chat message from a chatter, {username}, talking to you): {user_message}").text
                        await message.reply(resp)
                        save_history(username, user_message, resp)
                elif message.guild is None:
                    resp = chat.send_message(f"Respond relevantly to this chat message (it's a dm to you): {user_message}").text
                    await message.author.send(resp)
                    save_history(username, user_message, resp)
                else:
                    rannum = random.randint(1,300)
                    if rannum >= 301:
                        resp = chat.send_message(f"Try to respond relevantly to this chat message from {username}, based on the discord chat history (They are usually not talking to you): {user_message}").text
                        await message.reply(resp)
                        save_history(username, user_message, resp)
                    elif rannum == -1:
                        resp = chat.send_message(f"Make up a random reason to timeout this chatter, {username}, for 5 minutes based on their message: {user_message}").text
                        await message.reply(resp)
                        await message.author.timeout(timedelta(minutes=5),reason = resp)
                        save_history(username, user_message, resp)
                    else:
                        save_history(username, user_message, "")
                        
            else:
                save_history(username, user_message, "")
                await bot.process_commands(message)


    #Reset chat bot
    @bot.command()
    async def resetchat(ctx):
        global chat
        chat = responses.create_chat()
        await ctx.send("My memory is wiped 🥀")





    @bot.command()
    async def help(ctx):
        await ctx.message.reply("YOU'RE NOT GETTING ANY HELP FOR THIS ONE")


    
    bot.run(TOKEN)
