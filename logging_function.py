import discord
from discord.ext import commands
from datetime import datetime
# custom_commands is a file that handles commands i've created, check custom_commands.py for code
from custom_commands import logging_preferences

class CustomLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def log_event(self, guild, channel_id, title, description, color):
        """Send an embed log message to the specified channel."""
        channel = guild.get_channel(channel_id)
        if channel:
            embed = discord.Embed(
                title=title,
                description=description,
                color=color,
                timestamp=datetime.utcnow()
            )
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        for channel_id, events in logging_preferences.items():
            if "join" in events:
                await self.log_event(guild, channel_id, "User Joined", f"{member.mention} has joined the server.", discord.Color.green())

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        for channel_id, events in logging_preferences.items():
            if "leave" in events:
                await self.log_event(guild, channel_id, "User Left", f"{member.mention} has left the server.", discord.Color.red())

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = member.guild
        for channel_id, events in logging_preferences.items():
            # Voice channel join
            if before.channel is None and after.channel and "voice_join" in events:
                await self.log_event(guild, channel_id, "Voice Join", f"{member.mention} joined voice channel {after.channel.name}.", discord.Color.green())
            # Voice channel leave
            elif after.channel is None and before.channel and "voice_leave" in events:
                await self.log_event(guild, channel_id, "Voice Leave", f"{member.mention} left voice channel {before.channel.name}.", discord.Color.red())
            # Voice mute/unmute
            elif before.self_mute != after.self_mute:
                if after.self_mute and "voice_mute" in events:
                    await self.log_event(guild, channel_id, "Voice Mute", f"{member.mention} was muted.", discord.Color.purple())
                elif not after.self_mute and "voice_unmute" in events:
                    await self.log_event(guild, channel_id, "Voice Unmute", f"{member.mention} was unmuted.", discord.Color.from_rgb(255, 182, 193))
            # Voice deafen/undeafen
            elif before.self_deaf != after.self_deaf:
                if after.self_deaf and "voice_deafen" in events:
                    await self.log_event(guild, channel_id, "Voice Deafen", f"{member.mention} was deafened.", discord.Color.orange())
                elif not after.self_deaf and "voice_undeafen" in events:
                    await self.log_event(guild, channel_id, "Voice Undeafen", f"{member.mention} was undeafened.", discord.Color.light_grey())

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        guild = message.guild
        for channel_id, events in logging_preferences.items():
            if "message" in events:
                await self.log_event(guild, channel_id, "Message Sent", f"{message.author.mention} sent a message in {message.channel.mention}: {message.content}", discord.Color.blue())

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        guild = message.guild
        for channel_id, events in logging_preferences.items():
            if "message_delete" in events:
                await self.log_event(guild, channel_id, "Message Deleted", f"A message by {message.author.mention} was deleted in {message.channel.mention}.", discord.Color.yellow())

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = before.guild
        for channel_id, events in logging_preferences.items():
            # Nickname change
            if before.nick != after.nick and "nickname" in events:
                await self.log_event(guild, channel_id, "Nickname Change", f"{before.mention} changed their nickname from {before.nick} to {after.nick}.", discord.Color.from_rgb(173, 216, 230))

            # Role add/remove
            added_roles = [role for role in after.roles if role not in before.roles]
            removed_roles = [role for role in before.roles if role not in after.roles]
            for role in added_roles:
                if "role_add" in events:
                    await self.log_event(guild, channel_id, "Role Added", f"{before.mention} was given the role {role.name}.", discord.Color.dark_grey())
            for role in removed_roles:
                if "role_delete" in events:
                    await self.log_event(guild, channel_id, "Role Removed", f"{before.mention} lost the role {role.name}.", discord.Color.dark_red())

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        for channel_id, events in logging_preferences.items():
            if "ban" in events:
                await self.log_event(guild, channel_id, "User Banned", f"{user.mention} was banned from the server.", discord.Color.greyple())

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        for channel_id, events in logging_preferences.items():
            if "unban" in events:
                await self.log_event(guild, channel_id, "User Unbanned", f"{user.mention} was unbanned in the server.", discord.Color.magenta())

async def setup(bot):
    await bot.add_cog(CustomLogger(bot))
