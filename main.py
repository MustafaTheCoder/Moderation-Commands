@client.command() 
@commands.has_permissions(manage_messages=True) #checking if the user has "manage_messages" permission = true
async def purge(ctx, amount=2): #naming the command ;-;
    await ctx.channel.purge(limit=amount) #the actuall way to purge messages is this
    await ctx.send(f"{amount} Messages Purged Successfully.") #it will send a message after purging if you use the command

@client.command(aliases = ["slowmode"]) #an aliases for the command
@commands.has_permissions(manage_channels=True) #checking the perms for manage_channels
async def sm(ctx, seconds: int): #defining seconds as int
    await ctx.channel.edit(slowmode_delay=seconds) #editing the slowmode of the channel to your input
    await ctx.send(f"Slowmode Updated to {seconds} Seconds.") #sends a msg when edited the channel's slowmode

@client.command() #this is the kick command 
@commands.has_permissions(kick_members=True) #checking the perms for "kick_members" = true
async def kick(ctx, member: discord.Member, *, reason): #defining member as discord.Member and taking a reason 
    await member.kick(reason=reason) #kicking the member you mentioned and returning the reason you gave
    await ctx.send(f"{member.name} was kicked.") #sending a msg after kicking the member

@client.command() #this is the ban command!
@commands.has_permissions(ban_members=True) #checking perms for the "ban_members" = true
async def ban(ctx, member: discord.Member, *, reason): #defining member as discord.Member
    await member.ban(reason=reason) #banning a member you mentioned for the reason given
    await ctx.send(f"{member.name} was banned.") #sending the msg after the operation


@client.command() #this is the mute command
@commands.has_permissions(manage_messages=True) #checking if has "manage_messages" = true
async def mute(ctx, member: discord.Member, *, reason=None): #defining stuff ;-;
    guild = ctx.guild #making a variable for ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted") #giving the user muted role when he/she is muted

    if not mutedRole: #checking if there is no role name "Muted" in the guild
        mutedRole = await guild.create_role(name="Muted") #this line will create the role

        for channel in guild.channels: #perms for the muted member
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False,
                                          read_message_history=True,
                                          read_messages=False)

    await member.add_roles(mutedRole, reason=reason) #this will add the muted role to the member for the given reason
    await ctx.send(f"Muted {member.mention} for reason {reason}") #will return this message after the operation
    await member.send(f"You were muted in the server {guild.name} for {reason}" #this line will send you a dm saying you were muted
                      )
    




@client.command() #this is the unmute command
@commands.has_permissions(manage_messages=True) #checking perms
async def unmute(ctx, member: discord.Member): #defining stuff
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted") #checking if the member you mentioned has the muted role

    await member.remove_roles(mutedRole) #removing the muted role
    await ctx.send(f"Unmuted {member.mention}") #returning this as a message after the operation
    await member.send(f"You were unmuted in the server {ctx.guild.name}") #this line will send you a dm saying you are unmuted bla bla bla


