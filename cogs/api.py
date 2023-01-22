import discord
from discord.ext import commands
import openai

class APICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def generate_text(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
        )
        return response["choices"][0]["text"]
      
async def setup(bot):
	await bot.add_cog(APICog(bot))
