import os, discord
from discord.ext import commands
from dotenv import load_dotenv

pfx = ','
bot = commands.Bot(command_prefix = pfx, 
help_command = None)

@bot.event
async def on_ready():
  print('suede is online')

# help command
@bot.command()
async def help(ctx):
  embed = discord.Embed(title = '*help*', description = '`utility , moderation`', colour = 0x36393F)
  await ctx.send(embed = embed)

# utility command
@bot.command()
async def utility(ctx):
  embed = discord.Embed(title = '*utility*', description = '` ping , say , clear , avatar , membercount ,    \n userinfo , servericon , embed , send , perks   \n note `', colour = 0x36393F)
  await ctx.send(embed = embed)

# util cmds

# ping command
@bot.command()
async def ping(ctx):
  ping = round (bot.latency * 100)
  embed = discord.Embed(title = '*ping*', description = f'`{ping}ms`', colour = 0x36393F)
  await ctx.send(embed = embed)
  
# say command
@bot.command()
async def say(ctx, *, text):
  message = ctx.message
  await message.delete()
  await ctx.send(f"{text}")
  
# clear command
@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit = amount + 1)
  
# avatar command
@bot.command()
async def avatar(ctx, user : discord.Member = None):
  if user == None:
    user = ctx.author
    useravatar = user.avatar_url
    embed = discord.Embed(colour = 0x36393F)
    embed.add_field(name = f"{user.name}'s avatar", value = f'**[download]({user.avatar_url})**')
    embed.set_image(url = useravatar)
    await ctx.send(embed = embed)

# membercount command
@bot.command()
async def membercount(member):
  embed = discord.Embed(title = '*count*', description = f'{member.guild.member_count}', colour = 0x36393F)
  await member.send(embed = embed)

# userinfo command
@bot.command()
async def userinfo(ctx, member : discord.Member = None):
  member = member or ctx.author
  embed = discord.Embed(title = f"*{member}'s info*",colour = 0x36393F)
  embed.add_field(inline = False, name = '**id:**', value = f'`{member.id}`')
  embed.add_field(inline = False, name = '**created at:**', value = member.created_at.strftime('`%#d %B %Y`'))
  embed.add_field(inline = False, name = '**joined at:**', value = member.joined_at.strftime('`%#d %B %Y`'))
  await ctx.send(embed = embed)

# server icon command
@bot.command()
async def servericon(ctx):
  embed = discord.Embed(colour = 0x36393F)
  embed.add_field(name = f"{ctx.guild.name}'s icon", value = f'**[download]({ctx.guild.icon_url})**')
  embed.set_image(url = ctx.guild.icon_url)
  await ctx.send(embed = embed)

# embed command
@bot.command()
async def embed(ctx, *, text):
  embed = discord.Embed(colour = 0x36393F, description = f'{text}')
  message = ctx.message
  await message.delete()
  await ctx.send(embed = embed)

# send command
@bot.command()
async def send(ctx):
  message = ctx.message
  await message.delete()
  await ctx.send('test')

# perks command
@bot.command()
async def perks(ctx):
  embed = discord.Embed(title = '*boost & inv perks*', colour = 0x36393F)
  embed.add_field(name = 'boost perks', value = '` 1x bst = custom role + rich role + pic perms \n 2x bst = ^ + lowmod + bypass gw reqs         `')
  embed.add_field(inline = False, name = 'invite perks', value = '` 5x invs = custom role + pic perms            \n 10x invs = ^ + lowmod + gang role            `')
  await ctx.send(embed = embed)

# note command
@bot.command()
async def note(ctx, *, text: str):
  await ctx.message.delete()
  msg = await ctx.send(text)
  await msg.pin()

# moderation command
@bot.command()
async def moderation(ctx):
  embed = discord.Embed(title = '*moderation*', description = '` addrole , removerole , createrole , kick , ban \n , mute , unmute , lock , unlock `', colour = 0x36393F)
  await ctx.send(embed = embed)

# addrole command
@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member:discord.Member, *, role:discord.Role = None):
  await member.add_roles(role)
  await ctx.send(f'{member} was given {role}')

# removerole command
@bot.command()
@commands.has_permissions(manage_roles = True)
async def removerole(ctx, member:discord.Member, *, role:discord.Role = None):
  await member.remove_roles(role)
  await ctx.send(f'{role} was taken from {member}')

@bot.command()
# createrole command
@commands.has_permissions(manage_roles = True)
async def createrole(ctx, *, role:str = None):
  guild = ctx.guild
  perms = discord.Permissions(permissions=0)
  await guild.create_role(name = role, permissions = perms)
  await ctx.send(f'{role} was created')

# kick command
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
  await member.kick(reason = reason)
  await ctx.send(f'{member} was kicked')

# ban command
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
  await member.ban(reason = reason)
  await ctx.send(f'{member.name} was banned')

# unban command
@bot.command()
@commands.has_permissions(ban_members=True)   
async def unban(ctx, id : int):
    member = await bot.fetch_user(id)
    await ctx.guild.unban(member)
    await ctx.send(f'{member} is unbanned')

# mute command
@bot.command()
@commands.has_permissions(manage_roles = True)
async def mute(ctx, member:discord.Member):
  role = ctx.guild.get_role(966268284611723327)
  role2 = ctx.guild.get_role(944391240546394112)
  await member.remove_roles(role2)
  await member.add_roles(role)
  await ctx.send(f'{member} was muted')

# unmute command
@bot.command()
@commands.has_permissions(manage_roles = True)
async def unmute(ctx, member : discord.Member):
  role = ctx.guild.get_role(966268284611723327)
  role2 = ctx.guild.get_role(944391240546394112)
  await member.add_roles(role2)
  await member.remove_roles(role)
  await ctx.send(f'{member} was unmuted')

# lock command
@bot.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx, *, reason = 'none'):
  channel = ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.get_role(962518215991377953))
  overwrite.send_messages = False
  await channel.set_permissions(ctx.guild.get_role(962518215991377953), overwrite = overwrite)
  embed = discord.Embed(title = 'locked', description = f'reason = {reason}', colour = 0x36393F)
  await channel.send(embed = embed)

# unlock command
@bot.command()
@commands.has_permissions(manage_channels = True)
async def unlock(ctx, *, reason = 'none'):
  channel = ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.get_role(962518215991377953))
  overwrite.send_messages = True
  await channel.set_permissions(ctx.guild.get_role(962518215991377953), overwrite = overwrite)
  embed = discord.Embed(title = 'unlocked', description = f'reason = {reason}', colour = 0x36393F)
  await channel.send(embed = embed)



# misc

# name ping
@bot.event
async def on_message(msg : discord.Message):
  if msg.author.id == bot.user.id:
    return
  if msg.content == 'owner':
    await msg.channel.send('<@942956338798010448>')
  await bot.process_commands(msg)
  
# events

# welcome message
@bot.event
async def on_member_join(member):
  channel = bot.get_channel(944112299151618128)
  await channel.send(f'{member.mention}, welc to saudi\n{member.guild.member_count}')

# error handling
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('wrong command')

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot.run(TOKEN)