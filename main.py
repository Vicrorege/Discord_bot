import discord

from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from time import sleep as s
from discord_components import DiscordComponents, Button, ButtonStyle

# Список матов.
mats = []
# Сдесь любой ID канала
setchl = 972216206608187513

# Префикс бота.
bot = Bot(command_prefix=".")
bot.remove_command('help')

@bot.event
async def on_ready():
	DiscordComponents(bot)
	print(f'{bot.user} is connected!')

	await bot.change_presence(status=discord.Status.online, activity=discord.Game(".help"))

@bot.event
async def on_message(message):
	await bot.process_commands(message)

	msg = message.content.lower()

	if msg in mats:
		await message.channel.purge(limit=1)
		await message.channel.send('Не матерись !!!')
		bw += 1

@bot.event
async def on_member_join(member):
	chljoinID = 975814799822843974
	channelJoin = bot.get_channel(chljoinID)

	await channelJoin.send(f"Чел {member} Зашёл к нам.")

@bot.event
async def on_member_remove(member):
	chlremoveID = 975814799822843974
	channelRemove = bot.get_channel(chlremoveID)
	

@bot.command()
async def hello(ctx):
	await ctx.send(f'Привет, {ctx.author.mention}')

@bot.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, ammout=10000):
	await ctx.channel.purge(limit = ammout)

@bot.command()
async def info(ctx):
	await ctx.channel.purge(limit=1)

	emb = discord.Embed(title = "Информация о боте", colour=discord.Color.green())

	emb.add_field(name='Создатель', value='TimAnt')
	emb.add_field(name='Официальный сервер', value='https://discord.gg/CP3ha2gk7A')
	emb.add_field(name='Обратная связь', value='TimAnt#4025, anteytim@gmail.com')

	emb.set_footer(text = "TimAnt#4025 - Разработчик", icon_url = "https://cdn.discordapp.com/avatars/915662010111389758/b6f0b63da255e06a00044987871d57ad.png?size=1024")

	await ctx.send(embed = emb)

@bot.command()
async def help(ctx):
	await ctx.channel.purge(limit = 1)

	emb = discord.Embed(title='Навигация по командам(* - Команда для админа)', colour=discord.Color.orange())

	emb.add_field(name='.hello', value='Приветствие')
	emb.add_field(name='.clear*', value='Очистка чата')
	emb.add_field(name='.info', value='Вся информация о боте')
	emb.add_field(name='.idea <"idea">', value='Идея. в""')
	emb.add_field(name='.help', value='Это окно')
	emb.add_field(name='.purging <ammout>*', value='Отчистка кокого-то кол-ва сообщений')
	emb.add_field(name='.addmat <mat>', value='Добавить мат в базу')
	emb.add_field(name='.spam1 <member>*', value='Спам участника в ЛС 1го уровня')
	emb.add_field(name='.spam2 <member>*', value='Спам участника в ЛС 2го уровня')
	emb.add_field(name='.spam3 <member>*', value='Спам участника в ЛС 3го уровня')
	emb.add_field(name='.give_admin <member>*', value='Команда выдачи администратора')
	emb.add_field(name='.give_role <member>*', value='Команда добавления роли')
	emb.add_field(name='.remove_role <member>*', value='Команда удаления роли')
	emb.add_field(name='.setchannel <id>*', value='Задать идентефикатор канала')

	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)

	await ctx.send(embed = emb)

@bot.command()
async def idea(ctx, kwargs):
	await ctx.channel.purge(limit = 1)

	channelID = 978347661730136124
	chlIDEA = bot.get_channel(channelID)
	emb = discord.Embed(title=f'Идея от {ctx.author.name}', colour=discord.Color.blue())

	emb.add_field(name =':', value = kwargs)

	await chlIDEA.send(embed = emb)

@bot.command()
@commands.has_permissions(administrator = True)
async def purging(ctx, arg):
	await ctx.channel.purge(limit=int(arg) + 1)

@bot.command()
@commands.has_permissions(administrator = True)
async def give_role(ctx, member:discord.Member):
	await ctx.send(
		embed = discord.Embed(title = "Выдать роль:"),
		components = [
			Button(style = ButtonStyle.blue, label = 'ПРИВЕЛЕГИЯ ТИП 3', emoji = '♻️'),
			Button(style = ButtonStyle.blue, label = 'ПРИВЕЛЕГИЯ ТИП 2', emoji = '♻️'),
			Button(style = ButtonStyle.blue, label = 'ПРИВЕЛЕГИЯ ТИП 1', emoji = '♻️'),
			Button(style = ButtonStyle.blue, label = 'МУТ', emoji = '♻️'),
		]
		)

	response = await bot.wait_for("button_click")
	if response.channel == ctx.channel:
		if response.component.label == "ПРИВЕЛЕГИЯ ТИП 3":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]		
			)
			r1 = await bot.wait_for("button_click")
			if r1.channel == ctx.channel:
				if r1.component.label == "Yes":
					trole = discord.utils.get(ctx.message.guild.roles, name = 'ПРИВЕЛЕГИЯ3')
					
					await member.add_roles(trole)
					await response.respond(content = "OK!!!")
		if response.component.label == "ПРИВЕЛЕГИЯ ТИП 2":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]		
			)
			r2 = await bot.wait_for("button_click")
			if r2.channel == ctx.channel:
				if r2.component.label == "Yes":
					twrole = discord.utils.get(ctx.message.guild.roles, name = 'ПРИВЕЛЕГИЯ2')
					
					await member.add_roles(twrole)
					await response.respond(content = "OK!!!")
		if response.component.label == "ПРИВЕЛЕГИЯ ТИП 1":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]
			)
			r3 = await bot.wait_for("button_click")
			if r3.channel == ctx.channel:
				if r3.component.label == "Yes":
					orole = discord.utils.get(ctx.message.guild.roles, name = 'ПРИВЕЛЕГИЯ1')

					await member.add_roles(orole)
					await response.respond(content = "OK!!!")
		if response.component.label == "АДМИН ":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]		
			)
			r4 = await bot.wait_for("button_click")
			if r4.channel == ctx.channel:
				if r4.component.label == "Yes":
					await response.respond(content = "OK!!!")

					arole = discord.utils.get(ctx.message.guild.roles, name = 'Админ/модер')
					mrm = member

					await mrm.add_roles(arole)
		if response.component.label == "МУТ":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]
			)
			r5 = await bot.wait_for("button_click")
			if r5.channel == ctx.channel:
				if r5.component.label == "Yes":
					mrole = discord.utils.get(ctx.message.guild.roles, name = 'mute')

					await member.add_roles(mrole)
					await response.respond(content = "OK!!!")

@bot.command()
@commands.has_permissions(administrator = True)
async def remove_role(ctx, member:discord.Member):
	await ctx.send(
		embed = discord.Embed(title = "Убрать роль:"),
		components = [
			Button(style = ButtonStyle.blue, label = 'ПРИВЕЛЕГИЯ ТИП 3', emoji = '♻️'),
			Button(style = ButtonStyle.blue, label = 'ПРИВЕЛЕГИЯ ТИП 2', emoji = '♻️'),
			Button(style = ButtonStyle.blue, label = 'ПРИВЕЛЕГИЯ ТИП 1', emoji = '♻️'),
			Button(style = ButtonStyle.blue, label = 'МУТ', emoji = '♻️'),
		]
		)

	response = await bot.wait_for("button_click")
	if response.channel == ctx.channel:
		if response.component.label == "ПРИВЕЛЕГИЯ ТИП 3":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]		
			)
			r1 = await bot.wait_for("button_click")
			if r1.channel == ctx.channel:
				if r1.component.label == "Yes":
					trole = discord.utils.get(ctx.message.guild.roles, name = 'ПРИВЕЛЕГИЯ3')

					await member.remove_roles(trole)
					await response.respond(content = "OK!!!")
		if response.component.label == "ПРИВЕЛЕГИЯ ТИП 2":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]		
			)
			r2 = await bot.wait_for("button_click")
			if r2.channel == ctx.channel:
				if r2.component.label == "Yes":
					twrole = discord.utils.get(ctx.message.guild.roles, name = 'ПРИВЕЛЕГИЯ2')
					
					await member.remove_roles(twrole)
					await response.respond(content = "OK!!!")
		if response.component.label == "ПРИВЕЛЕГИЯ ТИП 1":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]		
			)
			r3 = await bot.wait_for("button_click")
			if r3.channel == ctx.channel:
				if r3.component.label == "Yes":
					orole = discord.utils.get(ctx.message.guild.roles, name = 'ПРИВЕЛЕГИЯ1')
					
					await member.remove_roles(orole)
					await response.respond(content = "OK!!!")
		if response.component.label == "МУТ":
			await ctx.send(
				embed = discord.Embed(title = "Ты уверен?"),
				components = [
					Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
					Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
				]		
			)
			r4 = await bot.wait_for("button_click")
			if r4.channel == ctx.channel:
				if r4.component.label == "Yes":
					mrole = discord.utils.get(ctx.message.guild.roles, name = 'mute')
					
					await member.remove_roles(mrole)
					await response.respond(content = "OK!!!")

@bot.command()
@commands.has_permissions(administrator = True)
async def give_admin(ctx, member:discord.Member):
	await ctx.send(
		embed = discord.Embed(title = "Ты уверен?"),
		components = [
			Button(style = ButtonStyle.green, label = 'Yes', emoji = '✔️'),
			Button(style = ButtonStyle.red, label = 'No', emoji = '❌')
	]		
		)

	response = await bot.wait_for("button_click")
	if response.channel == ctx.channel:
		if response.component.label == "Yes":
			await response.respond(content = "OK!!!")
			
			arole = discord.utils.get(ctx.message.guild.roles, name = 'Админ/модер')
			mrm = member
			
			await mrm.add_roles(arole)
		if response.component.label == "No":
			await response.respond(content = "OTMEHA!!!")
			

@bot.command()
async def addmat(ctx, arg):
	mats.append(arg)
	print(mats)

	await ctx.send('Спасибо за добавление мата в базу: '+ arg)
	
	s(2)
	
	await ctx.channel.purge(limit = 2)

@bot.command()
@commands.has_permissions(administrator = True)
async def spam1(ctx,member:discord.Member):
	await ctx.channel.purge(limit = 1)

	for i in range(25):
		await member.send('spam spam spam')

@bot.command()
@commands.has_permissions(administrator = True)
async def spam2(ctx,member:discord.Member):
	await ctx.channel.purge(limit = 1)

	for i in range(50):
		await member.send('spam spam spam spam spam spam')

# @bot.command()
# @commands.has_permissions(administrator = True)


@bot.command()
async def ideaAuthor(ctx, arg):
	aid = 915662010111389758
	Aur = bot.get_user(aid)
	
	await Aur.send(embed = discord.Embed(title = 'Идея от: ' + ctx.author.name + ' : ' + arg))

@bot.command()
@commands.has_permissions(administrator = True)
async def setchannel(ctx, arg):
	await ctx.channel.purge(limit=1)
	
	global setchl
	
	setchl = int(arg)
	
	return setchl
	
@bot.command()
@commands.has_permissions(administrator = True)
async def sendout(ctx, arg):
	await ctx.channel.purge(limit=1)
	
	global setchl
	
	chlid=setchl
	chl=bot.get_channel(chlid)
	
	await chl.send(arg)

# Токен бота/Bot token
bot.run(' ')