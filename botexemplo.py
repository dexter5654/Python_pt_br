import discord.py
from discord.ext import commands, tasks
from discord import errors
from itertools import cycle 

client=commands.Bot(command_prefix='!')
# Events 
@client.event
async def on_ready():
	print('seu bot esta online') 		
    change_status.start()
	
#|Status|#

bot_status = cycle(['status da sua escolha '])

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))#script lara status do bot 
    

	
@client.event
async def on_member_join(member):
	await ctx.send('Seja bem vindo {}'.format(member))
	#Codigo que indentifica quando um usuario (member) entra na guild e manda no canal de texto em que aquele member entrou 
	
	
	
# Comandos 
@client.command()
async def '''nome do comando ''' (ctx):
	#script do comando
	
@client.command()
async def avatar(ctx, user : discord.User):
	''''ctx' é a invocação do comando , já o 'user' são os parametros para executar o comando , nesse caso vc precisa de um esclarecer o usuario para poder ver sue avatar e é is
	que o 'discord.User' faz  ''''
	embed = discord.embed(title = f"Avatar de {user.name}{user.discriminator}", colour = discord.Colour.green())
	#Aqui vc define o titulo , a descrição  e a cor da sua embed 
	embed.set_image(url= user.avatar_url)
	#aqui vc seta uma imagem pela url 
	embed.set_foother(url=ctx.author.avatar_url, text = fRequisitado por {ctx.author.name})
	# e aqui vc consegue colocar um author na sua embed 
	
# Bem , isso aqui em baixo é simplesmente uma gambiarra que eu fiz pra funcionar caso vc não colocar o "user" na hora de executar o comando 

@avatar.error
async def avatar_error(ctx, error):
	if isistance(error, commands.MissingRequiredArgumets):
		embed = discord.embed(title = f"Avatar de {ctx.author.name}{ctx.author.discriminator}", colour = discord.Colour.green())
		embed.set_image(url= ctx.author.avatar_url)
		embed.set_foother(url=ctx.author.avatar_url, text = fRequisitado por {ctx.author.name})
		
# Mensagens automaticas 

@client.event
async def on_message(message):
	if message.author == client.user :
		return
	
	if message.content.startswith('Olá):
		#isso identifica  se a ultima mensagem foi igual a "Olá"
		await channel.send("Olá amigo")	
    # envia uma mensagem 
																
																
																
	 await client.process.commands(message)
								  
							
	
	
	
	
client.run('token')
	
