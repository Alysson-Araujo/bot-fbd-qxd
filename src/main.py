import discord, random, time, asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = ">", case_insensitive = True)

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

### Notificar os vídeos de instalação do PostgreSQL
@client.command()
async def notificar_video(ctx):
 count = 0 
 while True:
    count += 1
    canal = client.get_channel(852273456108142632)
    await asyncio.sleep(1) # em 24 horas ele notifica os usuários = 86400 segundos
    await canal.send(f"""Olá alunos do <@&892512310042718208> , sejam bem vindos ao servidor do discord da """+
                    """ disciplina Fundamentos de banco de dados! """+"\n"+"""A pedido da professora"""+
                    """ Lívia, peço a todos que vejam estes vídeos nos quais explicamos como instalar"""+
                    """ o PostgreSQL e o PGAdmin4. Em caso de dúvidas, fale conosco no canal de chat referente"""+
                    """ a sua turma. Para isso basta nos mencionar com <@&842022732060557312> ou <@&842025228649627688>"""+
                    """ nos canais de chat referentes a sua turma. Segue os links dos vídeos"""+
                    """ abaixo:"""+"\n"+"https://youtu.be/f1J_iiNLp_M "+"\n"+"https://youtu.be/oilARCECtAg")
    #await canal.send("https://youtu.be/f1J_iiNLp_M")
    #await canal.send("https://youtu.be/oilARCECtAg")
    break
    
    

client.run('ODk0NDA0MjQ4MTg2NTI3ODI0.YVpg3Q.qH6lwaXZ3D0aWtf_Pjzy0Wz8mu8')