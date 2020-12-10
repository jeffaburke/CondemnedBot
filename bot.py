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
    rulesEmbed = discord.Embed(color=discord.Color.blurple(), timestamp=datetime.datetime.now(), title="RULES")
    rulesEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    rulesEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
    rulesEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    rulesEmbed.add_field(name = 'Server Rules', value = '>>> :small_orange_diamond:Don\'t glitch/exploit/cheat/ in any way!\n:small_orange_diamond:Don\'t call out cheaters or suspicious players in game!\n:small_orange_diamond:Use F7 to report players or anything ( It goes right to server staff! )', inline = False)
    rulesEmbed.add_field(name = 'Discord Rules', value = '>>> :small_orange_diamond: Do not post NSFW content - We do not have a NSFW channel.\n:small_orange_diamond: Do not spam within any text channel.\n:small_orange_diamond: Toxic behavior is not welcome within our server.\n:small_orange_diamond: Ear-Rape, Screaming behavior within any Voice Channel is not welcome.\n:small_orange_diamond: Do not advertise - No unsolicited invite links or advertisements.\n:small_orange_diamond: Keep Racism / Homophobia / Sexism to a limit, do not cross the line.\n:small_orange_diamond: No Sharing Bot/ User Tokens / User Login Information.\n:small_orange_diamond: No Doxing - Do not post another member\'s personal information , not without his or her permission.\n:small_orange_diamond: DoS / DDoS is not allowed here , as well as discussions about how to do DoS and DDoS attacks.\n:small_orange_diamond: Don\'t break the Discord ToS. (Terms Of Service)', inline = False)
    await ctx.send(embed=rulesEmbed)
    memEmbed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(), title="CONFIRM")
    memEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    memEmbed.add_field(name = 'Agreeing to Server Rules', value = 'By clicking the :white_check_mark: below this message, you are agreeing & confirming to all server rules to gain access to Condemned Gaming!', inline = False)
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
            rulesEmbed.add_field(name = 'Server Rules', value = '>>> :small_orange_diamond:Don\'t glitch/exploit/cheat/ in any way!\n:small_orange_diamond:Don\'t call out cheaters or suspicious players in game!\n:small_orange_diamond:Use F7 to report players or anything ( It goes right to server staff! )', inline = False)
            rulesEmbed.add_field(name = 'Discord Rules', value = '>>> :small_orange_diamond: Do not post NSFW content - We do not have a NSFW channel.\n:small_orange_diamond: Do not spam within any text channel.\n:small_orange_diamond: Toxic behavior is not welcome within our server.\n:small_orange_diamond: Ear-Rape, Screaming behavior within any Voice Channel is not welcome.\n:small_orange_diamond: Do not advertise - No unsolicited invite links or advertisements.\n:small_orange_diamond: Keep Racism / Homophobia / Sexism to a limit, do not cross the line.\n:small_orange_diamond: No Sharing Bot/ User Tokens / User Login Information.\n:small_orange_diamond: No Doxing - Do not post another member\'s personal information , not without his or her permission.\n:small_orange_diamond: DoS / DDoS is not allowed here , as well as discussions about how to do DoS and DDoS attacks.\n:small_orange_diamond: Don\'t break the Discord ToS. (Terms Of Service)', inline = False)
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
    modEmbed.add_field(name = 'Moderator 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙢𝙚𝙣𝙩𝙨', value = '>>> :small_orange_diamond: 17+ years old.\n:small_orange_diamond: 500+ rust hours.•Active on our server.\n:small_orange_diamond: Active atleast 2-3 days per week.\n:small_orange_diamond: Active daily on discord.\n:small_orange_diamond: Can be online on most wipe days.\n:small_orange_diamond: Speaking spanish is + but not needed.', inline = False)
    await ctx.send(embed=modEmbed)
    adminEmbed = discord.Embed(color=discord.Color.red(), timestamp=datetime.datetime.now(), title="Administrator Applications")
    adminEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    adminEmbed.set_thumbnail(url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    adminEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    adminEmbed.add_field(name = 'Administrator Description', value = '>>> Admin roles are to watch over the reported players and help with server stuff. Admins are NOT allowed to PLAY on the server they are administrating on. Admins are granted access to server console logs which have handy tools to show cheaters and players or moderators breaking the server rules. Admins must try to be online on wipe days.', inline = False)
    adminEmbed.add_field(name = 'Administrator 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙢𝙚𝙣𝙩𝙨', value = '>>> :small_orange_diamond: 21+ years old.\n:small_orange_diamond: 1000+ rust hours.\n:small_orange_diamond: Active on our server.\n:small_orange_diamond: Active atleast 2-3 days per week.\n:small_orange_diamond: Active daily on discord.\n:small_orange_diamond: Can be online on most wipe days.\n:small_orange_diamond: Coding, plugins, cs and json files knowledge is a + but not needed.\n:small_orange_diamond: Speaking spanish is a + but not needed', inline = False)
    await ctx.send(embed=adminEmbed)
    intEmbed = discord.Embed(color=discord.Color.blue(), timestamp=datetime.datetime.now(), title="Interested in applying")
    intEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/754812042212278493/07545bb3c197a2ccc10eb201abf4dccc.png?size=256")
    intEmbed.add_field(name='Interested in applying', value='𝘔𝘰𝘥𝘦𝘳𝘢𝘵𝘰𝘳 𝘢𝘯𝘥 𝘢𝘥𝘮𝘪𝘯𝘴 𝘢𝘳𝘦 𝘵𝘰 𝘧𝘰𝘭𝘭𝘰𝘸 𝘢𝘭𝘭 𝘴𝘦𝘳𝘷𝘦𝘳 𝘳𝘶𝘭𝘦𝘴. 𝘐𝘧 𝘳𝘶𝘭𝘦𝘴 𝘢𝘳𝘦 𝘣𝘳𝘰𝘬𝘦𝘯 𝘺𝘰𝘶 𝘤𝘢𝘯 𝘣𝘦 𝘵𝘦𝘳𝘮𝘪𝘯𝘢𝘵𝘦𝘥 𝘢𝘯𝘥 𝘨𝘳𝘢𝘯𝘵𝘦𝘥 𝘢 𝘙𝘶𝘴𝘵 𝘈𝘥𝘮𝘪𝘯 𝘐𝘗 𝘉𝘢𝘯 𝘸𝘪𝘵𝘩 𝘵𝘩𝘦 𝘳𝘦𝘢𝘴𝘰𝘯 𝘸𝘩𝘺.𝘐𝘧 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘪𝘯𝘵𝘦𝘳𝘦𝘴𝘵𝘦𝘥 message <@325103571869892609> 𝘺𝘰𝘶𝘳 𝘪𝘯 𝘨𝘢𝘮𝘦 𝘯𝘢𝘮𝘦 𝘩𝘰𝘸 𝘮𝘢𝘯𝘺 𝘩𝘰𝘶𝘳𝘴 𝘺𝘰𝘶 𝘩𝘢𝘷𝘦 𝘰𝘯 𝘳𝘶𝘴𝘵 𝘢𝘯𝘥 𝘺𝘰𝘶\'𝘳𝘦 𝘢𝘨𝘦, 𝘐\'𝘭𝘭 𝘵𝘩𝘦𝘯 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘺𝘰𝘶 𝘪𝘧 𝘸𝘦 𝘥𝘦𝘤𝘪𝘥𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘢 𝘨𝘰𝘰𝘥 𝘧𝘪𝘵. Moderators have the chance to become admin if they succeed their roles for a certain period of time. Maturity, Time and Trust are a big thing.')
    await ctx.send(embed=intEmbed)

@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def howToVer(ctx):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    HTVEmbed = discord.Embed(color=discord.Color.gold(), timestamp=datetime.datetime.now())
    HTVEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/694103023508521001/37276cf5add1f22056c130c0fb0fb43f.png?size=128")
    HTVEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
    HTVEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    HTVEmbed.add_field(name = ' Verify you\'re discord with our servers to unlock the Discord Chat Text Channels.', value = '>>> You can do this by typing /verify in game chat and send that code to the discord bot that matches the server you\'re playing on listed under <@&694105892655726592>, finished.', inline = False)
    await ctx.send(embed=HTVEmbed)


@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator = True)
async def verify(ctx):
    mgs = []
    async for x in ctx.channel.history(limit=1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    verifyEmbed = discord.Embed(color=discord.Color.blurple(), timestamp=datetime.datetime.now(), title="Verify you're Discord with our Rust server.")
    verifyEmbed.set_footer(text = "Condemned Staff", icon_url="https://cdn.discordapp.com/avatars/694103023508521001/37276cf5add1f22056c130c0fb0fb43f.png?size=128")
    verifyEmbed.set_thumbnail(url="https://media.giphy.com/media/odFbqUcQPDVeE7bpnA/giphy.gif")
    verifyEmbed.set_author(name="Condemned Gaming Organization", icon_url="https://cdn.discordapp.com/attachments/660930305317797899/765051209618161665/image_5.gif")
    verifyEmbed.add_field(name = 'Follow the simple steps below.', value = '>>> 1) Go in game and type /verify\n2) Send the code to the "<@754812042212278493>" Bot or the "<@763247660743786557>" Bot on Discord for the server you are trying to verify on.\n', inline = False)
    verifyEmbed.add_field(name = 'This Unlocks:', value = '>>> • Discord Channels\n• Server skip queue\n• Colored Chat', inline = False)
    verifyEmbed.add_field (name = "Extra Information", value = 'Please note the Bots are on the top right side listed under <@&694105892655726592>\nIf you have any problems join the Help! Voice channel and DM <@&740631930189643826>\n', inline = False)
    await ctx.send(embed=verifyEmbed)

@verify.error
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


bot.run("key")
