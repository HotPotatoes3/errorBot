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
        crypticloop.start()
        check_corrupted_channels.start()
        print(f"{bot.user} is ready")
        try:
            synced = await bot.tree.sync()
        except Exception as e:
            print(e)

        
        
    global chat
    chat = responses.create_chat()


    corrupted_channels = {}


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
        "( hysteria:(shattered_voice) .type-(loss_of_self) )",
        "The painting shifts its gaze when you're alone.",
        "A cold hand reaches from beneath the bed.",
        "The reflection moves independently of you.",
        "You hear breathing, but no one is there.",
        "The static on the radio whispers your name.",
        "( anxiety:(fluttering_shadow) .type-(illusory_movement) )",
        "The flowers in the vase have turned black overnight.",
        "( apprehension:(distant_scream) .type-(unseen_violence) )",
        "Your name is carved into the dusty windowpane.",
        "( disquiet:(unblinking_stare) .type-(frozen_moment) )",
        "The music box plays even when it's unwound.",
        "( alarm:(rattling_chains) .type-(imprisoned_presence) )",
        "A child's laughter echoes from the empty attic.",
        "( trepidation:(sticky_floor) .type-(unknown_residue) )",
        "The book you were reading has new, disturbing passages.",
        "( suspicion:(locked_door_ajar) .type-(violated_space) )",
        "A single black feather lies on your pillow.",
        "( agitation:(flickering_lights) .type-(unstable_reality) )",
        "The scent of decay wafts through the air.",
        "( bewilderment:(impossible_geometry) .type-(cognitive_dissonance) )",
        "Your keys are in a place you don't remember leaving them.",
        "( unease:(repeating_numbers) .type-(pattern_of_dread) )",
        "The dog stares intently at a corner of the room.",
        "( creeping_fear:(cold_spot) .type-(lingering_presence) )",
        "A message appears on your phone from an unknown number: 'We're watching.'",
        "( sickening_dread:(viscous_liquid) .type-(organic_corruption) )",
        "The television turns on by itself, displaying only static.",
        "( mounting_terror:(shrill_whistle) .type-(piercing_silence) )",
        "You wake up with an inexplicable bruise.",
        "( paralyzing_fear:(suffocating_darkness) .type-(sensory_deprivation) )",
        "The shadows seem to have their own mass.",
        "( chilling_unease:(porcelain_crack) .type-(fragile_sanity) )",
        "You find a photograph of yourself that you don't recall taking.",
        "( gnawing_anxiety:(whispered_threat) .type-(verbal_violation) )",
        "The temperature in the room suddenly drops.",
        "( primal_fear:(bestial_growl) .type-(predatory_presence) )",
        "Your favorite song now sounds distorted and menacing.",
        "( existential_dread:(infinite_void) .type-(loss_of_meaning) )",
        "The floorboards creak as if someone is walking, even when you're alone.",
        "( unsettling_calm:(fixed_expression) .type-(hidden_intent) )",
        "You keep seeing the same unsettling symbol everywhere.",
        "( visceral_fear:(pulsating_vein) .type-(body_horror) )",
        "The wind outside sounds like someone crying.",
        "( creeping_insanity:(fragmented_thoughts) .type-(mental_fracture) )",
        "You find small, hand-stitched dolls appearing in unexpected places."
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
        print(f"ACTION TAKEN: {funnyNum}")
        guilds = bot.guilds
        random_guild = random.choice(guilds)
        if funnyNum < 300:
              # Get a list of all guilds the bot is in
            if guilds:
                  # Pick a random guild
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
        elif funnyNum < 500:
            eligible_channels = [
                channel for channel in random_guild.text_channels
                if channel.permissions_for(random_guild.me).manage_channels and channel.permissions_for(random_guild.me).manage_messages
            ]
            if eligible_channels:
                target_channel = random.choice(eligible_channels)
                original_name = target_channel.name
                corrupted_name = "WARNING-CORRUPT"
                try:
                    await target_channel.edit(name=corrupted_name)
                    print(f"Renamed channel {target_channel.name} to {corrupted_name} in {random_guild.name}")
                    corrupted_channels[target_channel.id] = {
                        'original_name': original_name,
                        'end_time': discord.utils.utcnow() + timedelta(minutes=5)
                    }
                except discord.Forbidden:
                    print(f"Bot lacks permissions to rename channel {target_channel.name} in {random_guild.name}")
                except discord.HTTPException as e:
                    print(f"Error renaming channel {target_channel.name}: {e} in {random_guild.name}")
        elif funnyNum > 980:
            for member in random_guild.members:
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
    
    async def revert_channel_name(channel_id):
        # """Reverts a channel name to its original name."""
        channel = bot.get_channel(channel_id)
        if channel:
            try:
                await channel.edit(name=corrupted_channels[channel_id]['original_name'])
                print(f"Reverted channel name of {channel.name} in {channel.guild.name}")
            except discord.HTTPException as e:
                print(f"Error reverting channel name: {e}")
            except discord.Forbidden:
                print(f"Missing permissions to revert channel name in {channel.name}")
        
    
    
                    
    @tasks.loop(seconds=60)  # Check every minute
    async def check_corrupted_channels():
        """Checks for expired corrupted channels and reverts their names."""
        expired_channels = []
        for channel_id, data in corrupted_channels.items():
            if data['end_time'] <= discord.utils.utcnow():
                expired_channels.append(channel_id)

        for channel_id in expired_channels:
            await revert_channel_name(channel_id)
            del corrupted_channels[channel_id]            
                    

    


    @bot.event
    async def on_message(message):
        global chat
        
        if message.author != bot.user:
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

            print(f"{username} said: '{user_message}' ({channel})")
            if user_message[0] != '!':
                if bot.user in message.mentions:
                    resp = chat.send_message(f"Respond relevantly to this chat message from a chatter,{username}, talking to you (<@1232601971870138409> is your ping, ignore it and avoid using it in your message): {user_message}").text
                    await message.reply(resp)
                elif message.reference is not None:
                    replied_message = await message.channel.fetch_message(message.reference.message_id)
                    if replied_message.author == bot.user:
                        resp = chat.send_message(f"Respond relevantly to this chat message from a chatter, {username}, talking to you): {user_message}").text
                        await message.reply(resp)
                elif message.guild is None:
                    resp = chat.send_message(f"Respond relevantly to this chat message (it's a dm to you): {user_message}").text
                    await message.author.send(resp)
                else:
                    rannum = random.randint(1,300)
                    if rannum == 300:
                        resp = chat.send_message(f"Try to respond relevantly to this chat message from {username}, based on the discord chat history (They are usually not talking to you): {user_message}").text
                        await message.reply(resp)
                    elif rannum == -1:
                        resp = chat.send_message(f"Make up a random reason to timeout this chatter, {username}, for 5 minutes based on their message: {user_message}").text
                        await message.reply(resp)
                        await message.author.timeout(timedelta(minutes=5),reason = resp)                        
            else:
                await bot.process_commands(message)
                
            # """Monitors messages in corrupted channels and kicks users."""
            if message.channel.id in corrupted_channels:
                if corrupted_channels[message.channel.id]['end_time'] > discord.utils.utcnow():
                    # Check if the sender has higher permissions than the bot
                    if message.author.top_role < message.guild.me.top_role:
                        try:
                            await message.author.kick(reason="You have angered us")
                            print(f"Kicked {message.author.name} from {message.guild.name} for posting in corrupted channel {message.channel.name}")
                        except discord.Forbidden:
                            print(f"Bot lacks permissions to kick {message.author.name} from {message.guild.name}")
                        except discord.HTTPException as e:
                            print(f"Error kicking {message.author.name}: {e}")
                    else:
                        await message.channel.send(f"I cannot kick you, {message.author.mention}, due to your higher permissions.")
                else:
                    # 5 minutes have passed, revert the channel name
                    await revert_channel_name(message.channel.id)
                    del corrupted_channels[message.channel.id] # remove entry from dict
            await bot.process_commands(message) # needed for commands.Bot


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
