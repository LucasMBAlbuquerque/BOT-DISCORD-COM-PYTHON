from discord.ext import commands

class Resposta(commands.Cog):
    """ Reage às mensagens """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
            
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'estou pronto! Estou conectado como {self.bot.user}')

def setup(bot):
    bot.add_cog(Resposta(bot))