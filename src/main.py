import discord, random
from discord.ext import commands

client = commands.Bot(command_prefix = "%", case_insensitive = True)

@client.event

async def on_ready():
    print('Entramos como {0.user}' .format(client))

### comandos do bot
### ctx -> contexto
### colocando um f antes da frase, significa que podemos colocar códigos dentro da frase
@client.command()    
async def teste_ola(ctx):
    await ctx.send(f'Olá, isso é um teste {ctx.author}')

### jogar dado
@client.command()
async def jogar_dado(ctx, number):
    random_number = random.randint(1,int(number))
    await ctx.send(f'O número que saiu do dado é {random_number}')



client.run('ODk0NDA0MjQ4MTg2NTI3ODI0.YVpg3Q.qH6lwaXZ3D0aWtf_Pjzy0Wz8mu8')