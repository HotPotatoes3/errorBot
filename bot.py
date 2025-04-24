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
                    
                    
                    


    def save_history(username, user_message, bot_response):
        # Read the existing lines
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = []

        # Append the new messages
        lines.append(f"{username}: {user_message}\n")
        lines.append(f"Bot: {bot_response}\n")

        # Trim to the last MAX_LINES
        if len(lines) > MAX_LINES:
            lines = lines[-MAX_LINES:]

        # Write back to the file
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            f.writelines(lines)


    


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

    # monitored_channels = {}
    # @bot.command()
    # async def monitor(ctx):
        
    #     role = None
    #     roleMade = False
    #     for i in ctx.guild.roles:
    #         if i.name == "GOJO REVIVE":
    #             roleMade = True
    #             role = i

    #     if not roleMade:
    #         role = await ctx.guild.create_role(name="GOJO REVIVE", colour=Colour.red(), mentionable=True)
        
    #     monitored_channels[ctx.channel.id] = datetime.now(timezone.utc)
    #     await ctx.send(f"I'm monitoring this channel for inactivity, you better start yapping you BUMS.")
  
    # @bot.tree.command(name='monitor', description='Monitor a channel')
    # async def monitor(interaction: discord.Interaction):
        try:
            role = None
            roleMade = False
            for i in interaction.guild.roles:
                if i.name == "GOJO REVIVE":
                    roleMade = True
                    role = i

            if not roleMade:
                role = await interaction.guild.create_role(name="GOJO REVIVE", colour=Colour.red(), mentionable=True)
            
            await interaction.response.send_message("I'm monitoring this channel for inactivity, you better start yapping you BUMS.")
        except Exception as e:
            print(e)
            await interaction.response.send_message("Failed")

    # @bot.command()
    # async def unmonitor(ctx):
        try:
            del monitored_channels[ctx.channel.id]
        except Exception as e:
            await ctx.send("This channel is not being monitored.")

        await ctx.send("This channel is not being monitored.")

    # @bot.tree.command(name='unmonitor', description='Unmonitor a channel')
    # async def unmonitor(interaction: discord.Interaction):
        try:
            del monitored_channels[interaction.channel.id]
        except Exception as e:
            await interaction.response.send_message("This channel is not being monitored.")

        await interaction.send_message("This channel is not being monitored.")




    #Reset chat bot
    @bot.command()
    async def resetchat(ctx):
        global chat
        chat = responses.create_chat()
        await ctx.send("My memory is wiped 🥀")
        
    @bot.tree.command(name='resetchat', description='Wipes Gojo Memory')
    async def resetchat(interaction: discord.Interaction):
        global chat
        chat = responses.create_chat()
        await interaction.response.send_message("My memory is wiped 🥀")

    user_roles_backup = {}
    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def imprison(ctx, member: discord.Member):
        prisoner_role = discord.utils.get(ctx.guild.roles, name="Prisoner")
        if not prisoner_role:
            prisoner_role = await ctx.guild.create_role(name="Prisoner")

        # Save roles and remove all except @everyone
        previous_roles = [role for role in member.roles if role != ctx.guild.default_role and role != prisoner_role]
        user_roles_backup[member.id] = [role.id for role in previous_roles]

        await member.edit(roles=[prisoner_role])
        await ctx.send(f"{member.mention} has been imprisoned.")

        # Create prison realm channel if it doesn't exist
        prison_channel = discord.utils.get(ctx.guild.text_channels, name="infinite-void")
        if not prison_channel:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                prisoner_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }
            await ctx.guild.create_text_channel("infinite-void", overwrites=overwrites)
            await ctx.send("Created channel: infinite-void")
        
    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def release(ctx, member: discord.Member):
        if member.id not in user_roles_backup:
            await ctx.send("No record of previous roles for this member.")
            return

        role_ids = user_roles_backup.pop(member.id)
        roles_to_restore = [ctx.guild.get_role(role_id) for role_id in role_ids if ctx.guild.get_role(role_id)]
        await member.edit(roles=roles_to_restore)
        await ctx.send(f"{member.mention} has been released and roles restored.")




    @bot.command()
    async def help(ctx):
        await ctx.message.reply("YOU'RE NOT GETTING ANY HELP FOR THIS ONE")


    
    bot.run(TOKEN)
