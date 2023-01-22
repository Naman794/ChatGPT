import discord 
from discord.ext import commands

Class Improve(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
      
  def improve_command(self):
     self.cursor.execute("SELECT DISTINCT user_input FROM chat_log")
     rows = self.cursor.fetchall()
     if rows:
         for row in rows:
             user_input = row[0]
             # Study the command and improve it
             print(f"Studying command: {user_input}")
             # code to study and improve command
             # code to create new command
     else:
         print(f"No previous data found to improve command")
        
  async def schedule_improve_command(self):
    await self.bot.wait_until_ready()
    while not self.bot.is_closed():
        self.improve_command()
        await asyncio.sleep(60*60*24) # runs every day
 

  def setup(bot):
     bot.add_cog(GPT3Cog(bot))
     bot.loop.create_task(GPT3Cog.schedule_improve_command(bot))

    
