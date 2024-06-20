import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Utilites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.avatar = self.bot.user.avatar.url
        
    @nextcord.slash_command(description="Replies with bot latency.")
    async def ping(self, interaction: Interaction):
        latency = int(self.bot.latency * 1000)
        embed = nextcord.Embed(
            title="Pong!",
            color=0x0000,
            description=f"""
            **Latency**
            > * **Latency:** {latency}ms
            """
)
        embed.set_thumbnail(url=self.avatar)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
        
def setup(bot):
    bot.add_cog(Utilites(bot))