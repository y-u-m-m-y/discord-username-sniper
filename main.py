'''
NOTE:

1. This might get your account locked or disabled, using an alt instead of main is recommended.

2. You need to have a premium subscription ( nitro ) on your account

3. It only snipes username and not discriminator, keep the discrim on your account before hand

Example - if you wanna snipe xyz#0001, then set your discrim to 0001 and leave the username to any random string 


lastly this is a simple code to claim a username idk why i made this


~ created by hold#1337

'''




import os
import sys
import json
import requests
import discord
from discord.ext import commands
import asyncio 
import time


tkn = input("[-] Enter Your Account Token: ")
pwd = input("[-] Enter Your Account Password: ") # this is required to change username
userid = input("[-] Enter Target User's ID who is holding the username currently: ")
user = input("[-] Enter the username ( without discrim ) to snipe: ")
discrim = input("[-] Enter Discrim : #")


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="no-prefix", case_insensitive=True, intents=intents, self_bot=True)
client.remove_command('help') 
headers = {"Authorization": tkn} 


req = requests.Session()

async def snap(usr:str, payload:str): 
  try:
    handshake = await client.user.edit(username=usr, password=payload)
    print(f"[~] Sniped {usr}#{discrim}")
    time.sleep(10)
    sys.exit() 
  except:
    print(f"[~] Failed to snipe {usr}#{discrim}")
    time.sleep(10)
    sys.exit() 

@client.event
async def on_ready(): 
  while True:
    await asyncio.sleep(1)
    r = req.get("https://discord.com/api/v9//users/{}".format(userid), headers=headers) 
    idk = r.json()
    usern = idk["username"]
    zdiscrim = idk["discriminator"] 
    if str(usern) != user or str(zdiscrim) != discrim: 
      await snap(user, pwd) 
    else:
      print(f"[~] {user}#{discrim} is still taken") 
      



client.run(tkn, bot=False)
