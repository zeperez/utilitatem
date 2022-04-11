import discord
from discord import app_commands
from discord.ext import commands


class DiscordUtilityCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="avatar")
    async def avatar_command(self, interaction: discord.Interaction) -> None:
        """Gets user's avatar"""
        await interaction.response.send_message("Hello World", ephemeral=True)
