import discord
from discord.ext import commands
import os


class UtilitatemBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=discord.Intents.all())
        self.load_cogs()

    async def on_ready(self):
        print(f"Logged as {self.user}")

    def load_cogs(self):
        for entry in os.listdir("cogs"):
            if os.path.isfile(entry) and entry[-3:] == ".py":
                self.load_extension(f"cogs.{entry[:-3]}")
