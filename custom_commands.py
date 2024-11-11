import discord
from discord import app_commands
from discord.ext import commands

# Placeholder for logging preferences (channel and selected events)
logging_preferences = {}  # {channel_id: [selected_events]}

class LogEventsDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Join", value="join"),
            discord.SelectOption(label="Leave", value="leave"),
            discord.SelectOption(label="Voice Join", value="voice_join"),
            discord.SelectOption(label="Voice Leave", value="voice_leave"),
            discord.SelectOption(label="Voice Mute", value="voice_mute"),
            discord.SelectOption(label="Voice Unmute", value="voice_unmute"),
            discord.SelectOption(label="Voice Deafen", value="voice_deafen"),
            discord.SelectOption(label="Voice Undeafen", value="voice_undeafen"),
            discord.SelectOption(label="Message", value="message"),
            discord.SelectOption(label="Message Delete", value="message_delete"),
            discord.SelectOption(label="Role Add", value="role_add"),
            discord.SelectOption(label="Role Delete", value="role_delete"),
            discord.SelectOption(label="Nickname", value="nickname"),
            discord.SelectOption(label="Ban", value="ban"),
            discord.SelectOption(label="Unban", value="unban"),
            discord.SelectOption(label="Kick", value="kick"),
            discord.SelectOption(label="Timeout", value="timeout"),
        ]

        super().__init__(placeholder="Select log events to track...", min_values=1, max_values=len(options), options=options)

    async def callback(self, interaction: discord.Interaction):
        selected_events = self.values
        channel_id = interaction.channel_id
        logging_preferences[channel_id] = selected_events

        await interaction.response.send_message(
            f"Logging events set for this channel: {', '.join(selected_events)}",
            ephemeral=True
        )

class LogSetupView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(LogEventsDropdown())

async def setup_log_command(bot):
    @bot.tree.command(name="log", description="Set up log events for this channel.")
    async def log(interaction: discord.Interaction):
        await interaction.response.send_message(
            "Select the log events you'd like to track for this channel:",
            view=LogSetupView(),
            ephemeral=True  # Only the user setting up the log will see the message
        )

async def setup(bot):
    await setup_log_command(bot)
