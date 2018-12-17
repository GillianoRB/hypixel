import discord
import datetime
from discord.ext import commands
from discord.ext.commands import BucketType
from discord.ext.commands import Bot
from discord.utils import get
import random
import asyncio
import time


uptime = datetime.datetime.utcnow()
Client = discord.Client()
bot = commands.Bot(command_prefix='$')
bot.remove_command('help')
lines = open(r'creepybot.txt').read().splitlines()

owner = ["244169411026485259"]


@bot.event
async def on_ready():
    print("The CreepyBot is online!")
    await bot.change_presence(game=discord.Game(name='Currently on ' + str(len(bot.servers)) +
                                                ' servers', type=2))


    

@bot.command(pass_context = True)
@commands.has_any_role('staff')
async def ban(member: discord.Member, days: int = 1000):
    await bot.ban(member, days)


@bot.command(pass_context=True, hidden=True)
async def setname(ctx, *, name):
    if ctx.message.author.id not in owner:
        return
    name = name.strip()
    if name != "":
        try:
            await bot.edit_profile(username=name)
        except:
            await bot.say("Failed to change name")
        else:
            await bot.say("Successfuly changed name to {}".format(name))
    else:
        await bot.send_cmd_help(ctx)

@bot.command(pass_context=True, hidden=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id not in owner:
        return
    game = game.strip()
    if game != "":
        try:
            await bot.change_presence(game=discord.Game(name=game))
        except:
            await bot.say("Failed to change game")
        else:
            await bot.say("Successfuly changed game to {}".format(game))
    else:
        await bot.send_cmd_help(ctx)

@bot.command(pass_context = True)
@commands.has_any_role('Special Role')
async def leave(ctx):
    await bot.send_message(ctx.message.author, "to invite me back copy this link (https://discordapp.com/api/oauth2/authorize?client_id=467728819835371540&permissions=0&scope=bot)")
    await asyncio.sleep(2)
    toleave = bot.get_server(ctx.message.server.id)
    await bot.leave_server(toleave)

@bot.command(pass_context = True)
async def bans(ctx):
    x = await bot.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "Those who got banned",
                          description = x, color = 0xFFFFF)
    return await bot.say(embed = embed)

@bot.event
async def on_message(message):
    memberID = "244169411026485259"
    person = await bot.get_user_info(memberID)
    if message.server is None and message.author != bot.user:
        await bot.send_message(person, f"{message.author} said thru my dm's '{message.content}'")
    elif 'fuck' in message.content.lower():
        bot.send_message(message.channel, f"{message.author} please stop that")
        await asyncio.sleep(4)
        tmp = await bot.send_message(message.channel, 'Clearing messages...')
        await bot.delete_message(message)
    await bot.process_commands(message)


       
@bot.command()
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " squared is " + str(squared_value))

@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)



@bot.command(pass_context=True)
async def serverinfo(ctx):
    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: 
        roles = roles[:50]
        roles.append('>>>> [50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0xFFFF);
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await bot.say(embed = join);

@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await bot.reply("{}".format(member.avatar_url))
        
@bot.command(description='Choices')
async def choose(*choices : str):
    await bot.say(random.choice(choices))

@bot.command(pass_context=True, hidden=True)
async def setavatar(ctx, url):
	if ctx.message.author.id not in owner:
		return
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r:
			data = await r.read()
	await bot.edit_profile(avatar=data)
	await bot.say("I changed my icon")

@bot.command(pass_context=True)
async def Money(ctx):
    edit = await bot.say("Calculating how many i earn :moneybag: give me 3 seconds")
    await asyncio.sleep(3)
    await bot.edit_message(edit, "200 SRD that is 26.82 USD each month")
    

@bot.command(pass_context = True)
async def flip(ctx):
    Special = 'Special'
    flip = random.choice (['Heads','Tails', Special])
    await bot.send_message(ctx.message.channel, flip)

@bot.command(pass_context=True)
async def yt(ctx, url):

    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await bot.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    player.start()

@bot.command(pass_context=True)
async def summon(ctx):
    author = ctx.message.author
    voice_channel = author.voice_channel
    await bot.join_voice_channel(voice_channel)

@bot.command()
async def help(ctx):
    await bot.say("help is not added yet contact demongilly to ask the commands")
                
@bot.command()
async def add(a: int, b: int):
    await bot.say(a+b)

@bot.command()
async def minus(a: int, b: int):
    await bot.say(a-b)

@bot.command()
async def times(a: int, b:int):
    await bot.say(a*b)

@bot.command()
async def divide(a: int, b:int):
    await bot.say(a^b)




@bot.command(pass_context=True)
async def DoneReadingRules(ctx):
    await bot.delete_message(ctx.message)
    await bot.say("Really?")
    await bot.add_reaction(message, '\U0001f44d')
    await bot.add_reaction(message, '\U0001f44e')

@bot.command(pass_context=True)
@commands.cooldown(1, 50, commands.BucketType.user)
async def Cat(ctx):
    await bot.delete_message(ctx.message)
    Picture = ["https://i.imgur.com/xFmNXWj.png", "https://i.imgur.com/5Y1OScF.png", "https://i.imgur.com/vv6Su8d.png", "https://i.imgur.com/CLANTSt.png", "https://i.imgur.com/FbrsPBT.png", "https://i.imgur.com/mfQGRLb.png", "https://i.imgur.com/vBIpg9l.png", "https://i.imgur.com/lUp0L3C.png", "https://i.imgur.com/yzHZBWz.png", "https://i.imgur.com/YbINCvc.png", "https://i.imgur.com/UryZYf3.png", "https://i.imgur.com/e0D1ORV.png", "https://i.imgur.com/pWHdHxO.png", "https://i.imgur.com/t6nE65v.png", "https://i.imgur.com/Yp2b9tD.png", "https://i.imgur.com/skURKzI.png", "https://i.imgur.com/4PhUY5b.png"]
    await bot.send_message(ctx.message.channel, random.choice(Picture))

@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong", description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await bot.say(embed=embed)



def get_uptime(brief=False):
    now = datetime.datetime.utcnow()
    delta = now - uptime
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if not brief:
        if days:
            fmt = '**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds'
        else:
            fmt = '**{h}** hours, **{m}** minutes, and **{s}** seconds'
    else:
        fmt = '**{h}**h, **{m}**m, **{s}**s'
        if days:
            fmt = '{d}d ' + fmt
    return fmt.format(d=days, h=hours, m=minutes, s=seconds)

@bot.command()
async def botuptime():
    embed = discord.Embed(
            title = (get_uptime()),
            )
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def RapBattle(ctx):
    await bot.say(random.choice(["Yo Let me go first Or are you just on the thirst On the Friday you will get beaten by my rhymes that got the times you will never see the raps when you got the maps... Your Turn Say Somthing After Do ?RapBattle", "Yo Your A Chicken In A Nugget you always sleep in a bucket", "Well DJ Put The Music Up :minidisc: oh let me tell you some thing when you ever got born you got blowned up by the horn you never get to see ppl in this clothes well because so all you wear is a bell"]))




@bot.command(pass_context=True)
async def logout(ctx):
    if ctx.message.author.id == "244169411026485259":
        embed = discord.Embed(
            title = 'Shutting down...',
            colour = discord.Colour.green()
        )
        await bot.say(embed=embed)
        await bot.logout()
    elif ctx.message.author.id == "257575046288113665":
        embed = discord.Embed(
            title = 'Shutting down...',
            colour = discord.Colour.green()
        )
        await bot.say(embed=embed)
        await bot.logout()
    else:
        embed = discord.Embed(
            title = 'Dont You Even Do That Again You Dont Wanna see whats Gonna Happen',
            colour = discord.Colour.red()
        )
        await bot.say(embed=embed)

@bot.command()
async def botinfo():
    msg = "Connected to "+str(len(bot.servers))+" servers | Connected to "+str(len(set(bot.get_all_members())))+" users. The bot invite link is [Click here](https://discordapp.com/oauth2/authorize?client_id=467728819835371540&scope=bot)"
    embed = discord.Embed(title="Bot Info", description=msg, color=0x000000)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def GEN(ctx):
    await bot.delete_message(ctx.message)
    await bot.say("Wrong Cmd Bro Its ?gen and btw acc will not work untill Creepergilly refills it")



@bot.command(pass_context=True)
async def Soccer(ctx):
    await bot.say(random.choice(["1-0",
                                "1-1",
                                "1-0",
                                "1-1",
                                "0-1",
                                "0-1"]))



@bot.command(pass_context=True)
async def CreeperFlip(ctx):
    await bot.say(random.choice([f"{ctx.message.author.name} has Head :scream: ",
                                                         f"{ctx.message.author.name} has 4 feets :scream: ",
                                                         f"{ctx.message.author.name} has Head :scream: ",
                                                         f"{ctx.message.author.name} has 4 feets :scream: ",
                                                         f"{ctx.message.author.name} has Special Creeper :scream: ",
                                                         f"{ctx.message.author.name} has Special Creeper :scream: "]))


@bot.command(pass_context=True)
async def LyingTest(ctx):
    await bot.say(random.choice(["you are a liar",
                                "you said the truth",
                                "you are a liar",
                                "you said the truth"]))

@bot.command(pass_context=True)
async def RandomLyingTest(ctx, user: discord.Member):
    await bot.say(random.choice([f"{user.name} is a liar",
                                f"{user.name} is a liar",
                                f"{user.name}  said the truth"]))

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def MathTest(ctx):
    embed = discord.Embed(title="Math Question 1", description='Question', color=0x00ff00)
    embed.set_author(name='5+5=')
    embed.add_field(name='A. 10', value='Answer Great', inline=False)
    embed.add_field(name='B. 0', value='Answer Great', inline=True)
    embed.add_field(name='C. 11', value='Answer Great', inline=False)
    embed.add_field(name='D. Not 1 of those :/', value='Answer Great', inline=True)
    my_message = await bot.say(embed=embed)
    if 'A' in message.content:
        await bot.send_message(message.channel, "you got an A+")
    if 'B' in message.content:
        await bot.send_message(message.channel, "you got an A-")
    if 'C' in message.content:
        await bot.send_message(message.channel, "you got an B")
    if 'D' in message.content:
        await bot.send_message(message.channel, "you got an F-")

    
      
    

@bot.command(pass_context=True)
async def help2(ctx):
    embed=discord.Embed(title="Help", description="------------", color=0x7100e1)
    embed.set_author(name=f"{ctx.message.author.mention} This Is The Second Help")
    embed.add_field(name='1. %Cat', value='------------', inline=False)
    embed.add_field(name='2. %Ghost', value='------------', inline=True)
    embed.add_field(name='3. %ticket text', value='Done', inline=False)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def PlayMe(ctx):
    await bot.say("'never' JK type $play to play with me")

@bot.command(pass_context=True)
async def purge(context, number : int):
    """Clear a specified number of messages in the chat"""
    await bot.purge_from(context.message.channel, limit=number)

				

@bot.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author

    await bot.say('{0} joined at {0.joined_at}'.format(member))

@bot.command(pass_context=True)
async def Appearance(ctx):
    if ctx.message.author.id == '244169411026485259':
        embed = discord.Embed(
            title = 'You Are The Bot Creator',
            colour = discord.Colour.green()
        )
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(
            title = 'You Are A No One That Tried To See If You Are Bot Creator',
            colour = discord.Colour.red()
        )
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def HelpMe(ctx):
    await bot.say("Help me i need more source code with python DM Creepergilly ")

@bot.command(pass_context=True)
async def Speed(ctx):
    await bot.say("faster then Race car")
    
@bot.command(pass_context=True)
async def OG(ctx):
    await bot.say("wrong server dude")


@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command(pass_context=True)
async def login(ctx,*, content):
    await bot.send_message(bot.get_channel("474018059070210049"), f"{ctx.message.author.mention} has logged in as {content}")
    await bot.send_message(ctx.message.author, "now read rules")
    roles = discord.utils.get(ctx.message.server.roles, name="Logged in")
    await bot.add_roles(ctx.message.author, roles)

@bot.command(pass_context=True)
@commands.cooldown(1, 50, commands.BucketType.user)
async def Ghost(ctx):
    await bot.delete_message(ctx.message)
    ScaryPic = ["https://i.imgur.com/1dYK7jq.png", "https://i.imgur.com/4LTNR1f.png", "https://i.imgur.com/88Uyl61.png", "https://i.imgur.com/hOqrerf.png", "https://i.imgur.com/QwkQb4v.png", "https://i.imgur.com/ofZ5HbQ.png", "https://i.imgur.com/QFdd8qQ.png", "https://i.imgur.com/h2edpqu.png", "https://i.imgur.com/d7JVNZz.png", "https://i.imgur.com/DyvBKHP.png"]
    await bot.send_message(ctx.message.channel, random.choice(ScaryPic))


@bot.command(pass_context=True)
async def Truth(ctx):
    await bot.say("to be fair Creepergilly is a noob")
    await asyncio.sleep(10)
    await bot.say("just kidding no one is a noob")

@bot.command(pass_context=True)
async def ticket(ctx,*, content):
    everyone_perms = discord.PermissionOverwrite(read_messages=False)
    my_perms = discord.PermissionOverwrite(read_messages=True)

    everyone = discord.ChannelPermissions(target=ctx.message.server.default_role, overwrite=everyone_perms)
    mine = discord.ChannelPermissions(ctx.message.author, overwrite=my_perms)
    test = await bot.create_channel(ctx.message.server, 'ticket', everyone, mine)
    await bot.delete_message(ctx.message)
    await asyncio.sleep(2)
    msg = 'Hello pls wait for staff to come'
    for servers in bot.servers:
        for channel in servers.channels:
            if channel.name == 'ticket':
                await bot.send_message(channel, msg)
 
@bot.command(pass_context=True)
async def removeticket(ctx):
    Ticketchannel = discord.utils.get(bot.get_all_channels(), server__name='ValsNet Private', name='ticket')
    await bot.delete_channel(ctx.message.channel)

@bot.command(pass_context = 1)
async def kick(context, user : discord.Member, *, reason : str = None):
    if context.message.author.server_permissions.administrator:
        if reason is None:
             reason = 'No given reason.'
             try:
                 await bot.kick(user)
                 await bot.send_message(context.message.channel, '[' + str(context.message.author.mention) + '] SUCCESSFULLY KICKED ' + str(user.mention))
             except discord.errors.Forbidden:
                 await bot.send_message(context.message.channel, '[' + str(context.message.author.mention) + '] UNSUCCESSFULLY KICKED ' + str(user.mention))
             except:
                 await bot.send_message(ctx.message.channel, '[' + str(context.message.author.mention) + '] ATTEMPTED TO KICK SOMEONE, BUT SOMETHING WENT WRONG.')
    else:
        await bot.say("you do not have perms")


@bot.command(pass_context=True)
async def ROLES(context):
    ''' Displays all roles/IDs '''
    roles = context.message.server.roles
    result = 'The roles are``` '
    for role in roles:
        result += role.name + '``` ' + role.id + ',``` '
    await bot.say(result)


@bot.command(pass_context=True)
async def verify(ctx):
    role = discord.utils.get(ctx.message.server.roles, name="Member")
    botmsg = f"you have been verified as {ctx.message.author.name} dont worry this will happen to all ppl that verified"
    await bot.send_message(ctx.message.author, botmsg)
    await bot.add_roles(ctx.message.author, role)

@bot.command(pass_context=True)
async def removeverify(ctx):
    role = discord.utils.get(ctx.message.server.roles, name="Member")
    botmsg = "you have removed ur member role"
    await bot.send_message(ctx.message.author, botmsg)
    await bot.remove_roles(ctx.message.author, role)

@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User UnMuted!", description="**{0}** was Unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)



@bot.command(pass_context=True)
@commands.has_any_role('Staff')
async def tempmute(ctx, member: discord.Member,*, content):
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await bot.say(f"{member} has been muted for 30 seconds reason: {content}")
    await bot.add_roles(member, role)
    await asyncio.sleep(30)
    await bot.say(f"{member} mute has been expired")
    await bot.remove_roles(member, role)

@bot.command(pass_context=True)
async def DM(ctx, member: discord.Member,*, content):
    if ctx.message.author.id == '244169411026485259':
        await bot.delete_message(ctx.message)
        await bot.send_message(member, content)

@bot.command(pass_context=True)
@commands.has_any_role('Staff')
async def warn(ctx, member: discord.Member,*, content):
    role = discord.utils.get(ctx.message.server.roles, name="Warning")
    msg = f'{member} has been warned and got the role Warning reason: {content}'
    for servers in bot.servers:
        for channel in servers.channels:
            if channel.name == 'mod-logs':
                await bot.send_message(channel, msg)
                await bot.add_roles(member, role)

@bot.command(pass_context=True)
@commands.has_any_role('staff')
async def report(ctx, member: discord.Member,*, content):
    role = discord.utils.get(ctx.message.server.roles, name="Warning")
    role2 = discord.utils.get(ctx.message.server.roles, name="Infraction")
    role3 = discord.utils.get(ctx.message.server.roles, name="Perm Infraction")
    if "Warning" not in author.roles:
        await bot.add_role(member, role)
        await bot.say(f"{member.mention} has been report for {content}")
    elif "Warning" in author.roles:
        await bot.add_role(member, role2)
        await bot.say(f"{member.mention} has been report for {content}")
    elif "Infraction" in author.roles:
        await bot.add_role(member, role3)
        await bot.say(f"{member.mention} has been report for {content}")
    elif "Perm Infraction" in author.roles:
        await bot.say("This guy has Perm Infraction and has been reported again now he is banned")
        await bot.ban(member)
 
@bot.command(pass_context=True)
@commands.has_any_role('Staff')
async def permmute(ctx, member: discord.Member,*, content):
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await bot.say(f"{member} has been perm muted reason: {content}")
    await bot.add_roles(member, role)

@bot.command(pass_context=True)
@commands.has_any_role('Staff')
async def removepermmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await bot.say(f"{member} has been removed from muted role")
    await bot.remove_roles(member, role)


@bot.command(pass_context=True)
async def nickme(ctx,*, content):
    await bot.say(f"{ctx.message.author.mention} has successfully changed his nickname")
    await bot.change_nickname(ctx.message, content)



@bot.command(pass_context=True)
@commands.has_any_role('Staff', 'Special Role')
async def say(self,*, content):
    await bot.delete_message(self.message)
    await bot.say(content)


@bot.command(pass_context=True)
async def sudo(ctx,*, content):
    if ctx.message.author.id == '244169411026485259':
        embed = discord.Embed(
            title = f"{ctx.message.author.name} is not allowed to use this command he has his own special command"
            )
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)
    elif ctx.message.author.id == '257575046288113665':
        embed = discord.Embed(
            title = f"{ctx.message.author.name} is not allowed to use this command he has his own special command"
            )
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)
    elif ctx.message.author.id == '413135950206599168':
        embed = discord.Embed(
            title = f"{ctx.message.author.name} is not allowed to use this command he has his own special command"
            )
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)
    elif ctx.message.author.id == '158392456746893312':
        embed = discord.Embed(
            title = f"{ctx.message.author.name} is not allowed to use this command he has his own special command"
            )
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(
            title = f"{ctx.message.author.name} Said",
            description = content
            )
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hypixelinfo(ctx):
    await bot.say ("**hypixel** is a minecraft server based on many fun minigames. Hypixel includes games such as Skywars, Bedwars and Build Battle. Hypixel has a lot of different communities, such as PvP, Building and roleplaying Hypixel also has different ranks and cosmetics. You can buy the ranks on store.hypixel.net where you can buy many more things than ranks. https://i.imgur.com/EEG244D.png")

@bot.command(pass_context=True)
async def hpachievements(ctx):
    await bot.say("Hypixel includes many achievements, there is achievements in EVERY gamemode except for PTL lobby games! Hypixel has AP or Achievement Points, where you gain Hypixel XP and cosmetics for completing achievements! https://i.imgur.com/WZGtqFE.png")

@bot.command(pass_context=True)
async def warningSudo(ctx,*, content):
    if ctx.message.role.has('Warning'):
        await bot.say('Oh No You Have Warning You Cant Use This ')
    else:
        await bot.say('Better')

@bot.command(pass_context=True)
async def TestBan(ctx):
    if ctx.message.author.server_permissions.administrator:
        await bot.say("This Is Just A Test SO Yeah")
    else:
        await bot.say("You Have No Perms")



bot.run(os.getenv{"TOKEN"})
