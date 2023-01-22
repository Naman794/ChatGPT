import discord
from discord.ext import commands, tasks


class ErrorHandlingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dat_cog = bot.get_cog("DatCog")
        self.loop.create_task(self.schedule_fix_errors())

    async def schedule_fix_errors(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            await asyncio.sleep(3600)  # run every hour
            self.fix_errors()

    def fix_errors(self):
        self.cursor.execute("SELECT command, error_message FROM errors")
        errors = self.cursor.fetchall()
        for error in errors:
            command, error_message = error
            # fix the error and update the command
            self.cursor.execute("UPDATE commands SET command = ? WHERE command = ?", (updated_command, command))
            self.conn.commit()
            self.cursor.execute("DELETE FROM errors WHERE command = ?", (command,))
            self.conn.commit()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            self.dat_cog.store_error(ctx.message.content, "Command not found.")
        else:
            self.dat_cog.store_error(ctx.message.content, error)

async def setup(bot):
	await bot.add_cog(ErrorHandlingCog(bot))
