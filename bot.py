import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
from discord import utils

Guild = object()
bot = commands.AutoShardedBot(command_prefix='!', activity=discord.CustomActivity(name='Do !rules and !verify'))
bot.remove_command('help')

class log:
    @staticmethod
    async def edit(Bmessage, Amessage, channelId):  # FIX
        #await bot.get_channel(756900212890534000).send(f'A message was edited in <#{channelId}> and it said `{Bmessage}` and now it says `{Amessage}`')
        pass

    @staticmethod
    async def delete(message, channelId):
        #logEmbed.add_field(name = 'Deleted Message', value = f'A message was deleted in <#{channelId}> and it said `{message}`')
        #await bot.get_channel(756900212890534000).send(embed=logEmbed)
        pass

class get:
    pass

@bot.event
async def on_ready():
    print("---Bot---")
    print("---Version 0.2.1---")
    print(bot.user.id)
    print("---is ready!---")

@bot.event
async def on_raw_reaction_add(payload):
    channel_id = payload.channel_id
    if channel_id == 753813381894504529:
        Message = await bot.get_channel(channel_id).fetch_message(payload.message_id)
        aEmbed = discord.Embed(color=discord.Color.from_rgb(
            0, 51, 102), title="Announcement")
        aEmbed.add_field(name='From Staff', value=Message.content)
        await bot.get_channel(753804945039425627).send(embed=aEmbed)
    else:
        pass

@bot.event
async def on_raw_message_delete(payload):
    message = payload.cached_message
    try:
        await log.delete(message.content, payload.channel_id)
    except AttributeError:
        await log.delete("Message Untraceable", payload.channel_id)

@bot.event
async def on_message_edit(before, after):
    print(before.content)
    try:
        await log.edit(before.content, after.content, after.channel.id)
    except AttributeError:
        await log.edit("Message Untraceable", after.content, after.channel.id)


@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def rules(ctx):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    rulesEmbed = discord.Embed(color=discord.Color.blurple(), title='Discord rules and Game rules can work one in the same.\n\nRULES', description = '>>> 🔸 Do not glitch, exploit, cheat, in any way!\n🔸 Do not call out cheaters, suspicious players, or rule breakers in game!\n🔸 Please follow specific server rules including the team limits on certain servers.\n🔸 Breaking specific server rules will result in a permanent ban from all our servers. \n🔸 Report cheaters, suspicious players, or rule breakers to a moderator or admin on Discord.\n🔸 Purposely false reporting someone will get you\'re self banned.\n🔸 Keep Racism / Homophobia / Sexism to you\'re self, do not cross the line or harass a player.\n🔸 Don\'t be too toxic in game or Discord. This could result in a permanent ban both Discord and game side.\n🔸 Keep discord and server chats clean and stay on specific game topics.\n🔸 Our servers are for gaming they are NOT personal chat rooms.\n🔸 Do not post NSFW content - We do not have a NSFW channel.\n🔸 Use the Discord channels properly, or you will be blocked from that channel or banned from the Discord.\n🔸 Ear-Rape, Screaming behavior is not welcome.\n🔸 Do not advertise - No unsolicited invite links or advertisements.\n🔸 IP grabbing and DOSing (even threats of doing so) will result in a swift ban with ZERO appeal chance.  (It is illegal under the Federal Computer Fraud and Abuse Act)\n\nPlease keep in mind our server moderators are chat moderators and only have access to mute players. Our admins are all adults and are not allowed to actually play. Our admins review player reports and watch over suspicious players and do server side work. Falsely accusing a staff member will result in a permanent ban or permanent mute we are very strict about that! If you think someone might be cheating and our admins don\'t ban them that\'s because there is lack of evidence or they are legit. We highly recommend Steam reporting a players steam account if you think they are cheating they will get a game ban pretty quickly if they actually are.')
    rulesEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    rulesEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
    rulesEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    #rulesEmbed.add_field(name = 'RULES', value = '>>> 🔸 Do not glitch, exploit, cheat, in any way!\n🔸 Do not call out cheaters, suspicious players, or rule breakers in game!\n🔸 Please follow specific server rules including the team limits on certain servers.\n🔸 Breaking specific server rules will result in a permanent ban from all our servers. \n🔸 Report cheaters, suspicious players, or rule breakers to a moderator or admin on Discord.\n🔸 Purposely false reporting someone will get you\'re self banned.\n🔸 Keep Racism / Homophobia / Sexism to you\'re self, do not cross the line or harass a player.\n🔸 Don\'t be too toxic in game or Discord. This could result in a permanent ban both Discord and game side.\n🔸 Keep discord and server chats clean and stay on specific game topics.\n🔸 Our servers are for gaming they are NOT personal chat rooms.\n🔸 Do not post NSFW content - We do not have a NSFW channel.\n🔸 Use the Discord channels properly, or you will be blocked from that channel or banned from the Discord.\n🔸 Ear-Rape, Screaming behavior is not welcome.\n🔸 Do not advertise - No unsolicited invite links or advertisements.\n🔸 IP grabbing and DOSing (even threats of doing so) will result in a swift ban with ZERO appeal chance.  (It is illegal under the Federal Computer Fraud and Abuse Act)', inline = False)
    await ctx.send(embed=rulesEmbed)
    memEmbed = discord.Embed(color=discord.Color.green(), title="CONFIRM")
    memEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    memEmbed.add_field(name = 'Agreeing to Server Rules', value = 'By clicking the :white_check_mark: below this message, you are agreeing & confirming to all server rules to gain access to Role assignment', inline = False)
    await ctx.send(embed=memEmbed)

@rules.error
async def rules_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        mgs = []
        async for x in ctx.channel.history(limit=1):
            mgs.append(x)
        await ctx.channel.delete_messages(mgs)
        try:
            
            rulesEmbed = discord.Embed(color=discord.Color.blurple(), timestamp=datetime.datetime.now(), title="RULES")
            rulesEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/694103023508521001/37276cf5add1f22056c130c0fb0fb43f.png?size=128")
            rulesEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
            rulesEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
            rulesEmbed.add_field(name = 'Server Rules', value = '>>> 🔸Don\'t glitch/exploit/cheat/ in any way!\n🔸Don\'t call out cheaters or suspicious players in game!\n🔸Use F7 to report players or anything ( It goes right to server staff! )', inline = False)
            rulesEmbed.add_field(name = 'Discord Rules', value = '>>> 🔸 Do not post NSFW content - We do not have a NSFW channel.\n🔸 Do not spam within any text channel.\n🔸 Toxic behavior is not welcome within our server.\n🔸 Ear-Rape, Screaming behavior within any Voice Channel is not welcome.\n🔸 Do not advertise - No unsolicited invite links or advertisements.\n🔸 Keep Racism / Homophobia / Sexism to a limit, do not cross the line.\n🔸 No Sharing Bot/ User Tokens / User Login Information.\n🔸 No Doxing - Do not post another member\'s personal information , not without his or her permission.\n🔸 DoS / DDoS is not allowed here , as well as discussions about how to do DoS and DDoS attacks.\n🔸 Don\'t break the Discord ToS. (Terms Of Service)', inline = False)
            await ctx.author.send(embed = rulesEmbed)
        except discord.Forbidden:
            await ctx.send(f'{ctx.author.mention}, I couldn\'t send a message to you.')

@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def staffApp(ctx):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    modEmbed = discord.Embed(color=discord.Color.gold(), timestamp=datetime.datetime.now(), title="Moderator Applications")
    modEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    modEmbed.set_thumbnail(url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    modEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    modEmbed.add_field(name = 'Moderator Description', value = '>>> Moderators roles are to watch over server chat with the ability to mute highly toxic players that are spamming server chat and the ability to kick or ban racists players or players threatening the server in any way for example a ddos threat we take serious and that player should be banned. Players who disrespect the server or staff repeatedly will then be giving a warning and tell them to leave if they don\'t like it here if it continues please mute them for 30 minutes, if they continue after you unmute them the decision is then up to you with kick, ban or permanent mute. If moderators find any problems after a wipe they need to report it to a admin immediately. Moderators are also welcomed to help new players that join the server and if any players need help with verifying their steam account with the discord. Moderators are to report any suspicious players to admins they will then be reviewed before the decision is made to place a ban.', inline = False)
    modEmbed.add_field(name = 'Moderator 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙢𝙚𝙣𝙩𝙨', value = '>>> 🔸 17+ years old.\n🔸 500+ rust hours.•Active on our server.\n🔸 Active atleast 2-3 days per week.\n🔸 Active daily on discord.\n🔸 Can be online on most wipe days.\n🔸 Speaking spanish is + but not needed.', inline = False)
    await ctx.send(embed=modEmbed)
    adminEmbed = discord.Embed(color=discord.Color.red(), timestamp=datetime.datetime.now(), title="Administrator Applications")
    adminEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    adminEmbed.set_thumbnail(url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    adminEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    adminEmbed.add_field(name = 'Administrator Description', value = '>>> Admin roles are to watch over the reported players and help with server stuff. Admins are NOT allowed to PLAY on the server they are administrating on. Admins are granted access to server console logs which have handy tools to show cheaters and players or moderators breaking the server rules. Admins must try to be online on wipe days.', inline = False)
    adminEmbed.add_field(name = 'Administrator 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙢𝙚𝙣𝙩𝙨', value = '>>> 🔸 21+ years old.\n🔸 1000+ rust hours.\n🔸 Active on our server.\n🔸 Active atleast 2-3 days per week.\n🔸 Active daily on discord.\n🔸 Can be online on most wipe days.\n🔸 Coding, plugins, cs and json files knowledge is a + but not needed.\n🔸 Speaking spanish is a + but not needed', inline = False)
    await ctx.send(embed=adminEmbed)
    intEmbed = discord.Embed(color=discord.Color.blue(), timestamp=datetime.datetime.now(), title="Interested in applying")
    intEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    intEmbed.add_field(name='Interested in applying', value='𝘔𝘰𝘥𝘦𝘳𝘢𝘵𝘰𝘳 𝘢𝘯𝘥 𝘢𝘥𝘮𝘪𝘯𝘴 𝘢𝘳𝘦 𝘵𝘰 𝘧𝘰𝘭𝘭𝘰𝘸 𝘢𝘭𝘭 𝘴𝘦𝘳𝘷𝘦𝘳 𝘳𝘶𝘭𝘦𝘴. 𝘐𝘧 𝘳𝘶𝘭𝘦𝘴 𝘢𝘳𝘦 𝘣𝘳𝘰𝘬𝘦𝘯 𝘺𝘰𝘶 𝘤𝘢𝘯 𝘣𝘦 𝘵𝘦𝘳𝘮𝘪𝘯𝘢𝘵𝘦𝘥 𝘢𝘯𝘥 𝘨𝘳𝘢𝘯𝘵𝘦𝘥 𝘢 𝘙𝘶𝘴𝘵 𝘈𝘥𝘮𝘪𝘯 𝘐𝘗 𝘉𝘢𝘯 𝘸𝘪𝘵𝘩 𝘵𝘩𝘦 𝘳𝘦𝘢𝘴𝘰𝘯 𝘸𝘩𝘺.𝘐𝘧 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘪𝘯𝘵𝘦𝘳𝘦𝘴𝘵𝘦𝘥 message <@325103571869892609> 𝘺𝘰𝘶𝘳 𝘪𝘯 𝘨𝘢𝘮𝘦 𝘯𝘢𝘮𝘦 𝘩𝘰𝘸 𝘮𝘢𝘯𝘺 𝘩𝘰𝘶𝘳𝘴 𝘺𝘰𝘶 𝘩𝘢𝘷𝘦 𝘰𝘯 𝘳𝘶𝘴𝘵 𝘢𝘯𝘥 𝘺𝘰𝘶\'𝘳𝘦 𝘢𝘨𝘦, 𝘐\'𝘭𝘭 𝘵𝘩𝘦𝘯 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘺𝘰𝘶 𝘪𝘧 𝘸𝘦 𝘥𝘦𝘤𝘪𝘥𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘢 𝘨𝘰𝘰𝘥 𝘧𝘪𝘵. Moderators have the chance to become admin if they succeed their roles for a certain period of time. Maturity, Time and Trust are a big thing.')
    await ctx.send(embed=intEmbed)

@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def gra(ctx):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    assignEmbed = discord.Embed(color=discord.Color.gold(), title="GAME ROLE ASSIGNMENT")
    assignEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    assignEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
    assignEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    assignEmbed.add_field(name = 'Why?', value = '*Assign yourself roles to view specific game channels. React with the specified game icon that you\'d like to view the text and voice channels for.\nLooking for additional roles? Please message <@325103571869892609> for more help.*', inline = False)
    assignEmbed.add_field(name = 'Games', value = f'<:rust:784324864739639296> <@&787872856348426240>\n<:siege:787872435709018132> <@&787872878179123200>\n<:fivem:784324844031967242> <@&787872829215342593>\n<:ark:784323982211285002> <@&787872808238579742>', inline = False)
    await ctx.send(embed=assignEmbed)

@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def csfm(ctx):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    csfmEmbed = discord.Embed(color=discord.Color.gold(), timestamp=datetime.datetime.now(), title="FiveM Server Coming Soon", description='We are excited to announce that we are currently working on developing a FiveM server, so get prepared because this is going to be a great addition to the Condemned Gaming Organization')
    csfmEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    csfmEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
    csfmEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    await ctx.send(embed=csfmEmbed)

@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def howToVerR(ctx):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    HTVEmbed = discord.Embed(color=discord.Color.gold())
    HTVEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/694103023508521001/37276cf5add1f22056c130c0fb0fb43f.png?size=128")
    HTVEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
    HTVEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    HTVEmbed.add_field(name = ' Verify you\'re discord with our servers to unlock the Discord Chat Text Channels.', value = '>>> You can do this by typing /verify in game chat and send that code to the discord bot that matches the server you\'re playing on listed under <@&694105892655726592>, finished.', inline = False)
    await ctx.send(embed=HTVEmbed)


@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def rverify(ctx):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    verifyEmbed = discord.Embed(color=discord.Color.blurple(), title="Verify you're Discord with our Rust server.")
    verifyEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/694103023508521001/37276cf5add1f22056c130c0fb0fb43f.png?size=128")
    verifyEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
    verifyEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    verifyEmbed.add_field(name = 'Follow the simple steps below.', value = '>>> 1) Go in game and type /verify\n2) Send the code to the servers bot in which you want to verify with.\n', inline = False)
    verifyEmbed.add_field(name = 'This Unlocks:', value = '>>> • Discord Channels\n• Server skip queue\n• Colored Chat', inline = False)
    verifyEmbed.add_field (name = "Extra Information", value = 'Please note the Bots are on the top right side listed under <@&694105892655726592>\nIf you have any problems join the Help! Voice channel and DM <@&740631930189643826>\n', inline = False)
    await ctx.send(embed=verifyEmbed)

@rverify.error
async def verify_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        mgs = []
        async for x in ctx.channel.history(limit=1):
            mgs.append(x)
        await ctx.channel.delete_messages(mgs)
        try:
            verifyEmbed = discord.Embed(color=discord.Color.blurple(), timestamp=datetime.datetime.now(), title="Verify you're Discord with our Rust server.")
            verifyEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
            verifyEmbed.set_thumbnail(url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
            verifyEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
            verifyEmbed.add_field(name = 'Follow the simple steps below.', value = '\n>>> 1) Go in game and type /verify\n2) Send the code to the "<@754812042212278493>" Bot or the "<@694072565165195265>" Bot on Discord for the server you are trying to verify on.', inline = False)
            verifyEmbed.add_field(name = 'This Unlocks:', value = '\n>>> • Discord Channels\n• Server skip queue\n• Colored Chat', inline = False)
            verifyEmbed.add_field (name = "Extra Information", value = 'Please note the Bots are on the top right side listed under <@&694105892655726592>\nIf you have any problems join the Help! Voice channel and DM <@&740631930189643826>', inline = False)
            await ctx.author.send(embed=verifyEmbed)
        except discord.Forbidden:
            await ctx.send(f'{ctx.author.mention}, I couldn\'t send a message to you.')

@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def clear(ctx, number=100, silent=''):
    mgs = []
    number = int(number) + 1
    async for x in ctx.channel.history(limit=number):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    silent = str(silent)
    if silent != 's':
        await ctx.channel.send(f'`{number-1} messages have been deleted!`')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('`You must be a Administrator to do this command!`')


@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def na(ctx, id):
    pass


@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def announce(ctx, *args):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    say = ' '.join(args)
    await ctx.send(say)


@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('`You must be a Administrator to do this command!`')


'''@bot.command(pass_context=True)
async def staffhelp(ctx):
    author = ctx.author
    help = discord.Embed(color=discord.Color.from_rgb(0, 51, 102))
    help.set_author(name='Heres all the commands')
    help.add_field(name='Commands', value='!clear - This is a Administrator only command that clears a certain amount of messages!\n!gully - Show\'s all of gully\'s social\'s\nThat\'s it so far!')

    try:
        await author.send(embed=help)
    except discord.Forbidden:
        await ctx.send(f'{author.mention}, I couldn\'t send a message to you.')
'''

@bot.command(pass_context=True)
@commands.has_any_role('Owner', "Administrator")
async def copy(ctx):
    author = ctx.author
    mgs = []
    async for x in ctx.channel.history(limit=2):
        mgs.append(x)
    await ctx.channel.send(author)
    await ctx.channel.send(mgs)
    # help = discord.Embed(color=discord.Color.gold())
    # help.set_author(name='#0001')
    # help.add_field(name='Announcement', value='')


bot.run("Njk0MTAzMDIzNTA4NTIxMDAx.XoGv0A.-97N8m1nPHa7Q3UvXAfd6TEhGrU")