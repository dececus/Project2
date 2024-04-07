import discord
from discord.ext import commands
from flower import flower
from shape import shape
from cloth import cloth
from side import side
from color import color

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.command()
async def info(ctx):
    await ctx.send("""
'Green' представляет собой инновационную систему, способная определять различные виды цветов по фотографиям.
Пользователи могут легко загружать изображения цветов, а затем получать их тип, название, а также значение.
Прикрепите фотографию своего растения: 
""")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")
            await ctx.send("Тип: ")
            await ctx.send(shape(model_path="./keras_modelShape.h5", labels_path="labelsShape.txt", image_path=f"./{attachment.filename}"))
            await ctx.send(cloth(model_path="./keras_modelCloth.h5", labels_path="labelsCloth.txt", image_path=f"./{attachment.filename}"))
            await ctx.send(side(model_path="./keras_modelSide.h5", labels_path="labelsSide.txt", image_path=f"./{attachment.filename}"))
            await ctx.send(color(model_path="./keras_modelColor.h5", labels_path="labelsColor.txt", image_path=f"./{attachment.filename}"))
            #await ctx.send("Название: ")
            #await ctx.send(flower(model_path="./keras_modelFlower.h5", labels_path="labelsFlower.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Вы забыли загрузить картинку")

bot.run("MTE1NTUwMDI1ODMzMjI1MDIyMg.G_QO1n.AL900VcvBPv7vwoA4Zh1Uyg-5f3I3kQkoCrOuE")