from io import BytesIO
from discord.ext import commands
from PIL import Image
import os
import discord.member


class procurado(commands.Cog):
    """ foto de perfil procurado """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def procurado(self, ctx, member: discord.Member = None):
        '''você como o criminoso mais procurado do faroeste'''
        if member == None:
            member = ctx.author
        
        procurado = Image.open(r"fotos/procurado.jpg")

        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        profilepic = profilepic.resize((305, 305))

        procurado.paste(profilepic, (79,219))

        procurado.save("procuradopic.jpg")

        await ctx.send( file = discord.File("procuradopic.jpg"))
    
        os.remove("procuradopic.jpg")

def setup(bot):
    bot.add_cog(procurado(bot))