import discord
import asyncio
import sqlite3
import os
import math
import csv
from evetool import universemap,price,serverinfo

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    while message.content[-1]==' ':
        message.content=message.content[0:len(message.content)-1]
    if message.content.startswith('!message'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!hit'):
    	orders=message.content.split()
    	orderSize = len(orders)
    	if not orderSize==3:
    		reply = '__Please input two system names.__'
    	else:
    		reply = universemap.inOneJump(orders[1],orders[2])
    	await client.send_message(message.channel, reply)

    elif message.content.startswith('!jita'):
    	orders = message.content
    	orderSize = len(orders)
    	if orderSize<7:
    		reply = '__Please input one item name.__'
    	else:
    		reply = price.howmuch(orders[6:],'Jita')
    	await client.send_message(message.channel, reply)

    elif message.content.startswith('!osy'):
    	orders = message.content
    	orderSize = len(orders)
    	if orderSize<6:
    		reply = '__Please input one item name.__'
    	else:
    		reply = price.howmuch(orders[5:],'OSY-UD')
    	await client.send_message(message.channel, reply)

    elif message.content.startswith('!server'):
        await client.send_message(message.channel, serverinfo.serverinfo())
client.run('Token')