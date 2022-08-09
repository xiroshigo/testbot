from telethon import TelegramClient, events, sync
from telethon.errors import rpcbaseerrors
import time
##
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
#
import random
import time
import os, sys
import asyncio
import random
import wikipedia 
import requests
from collections import deque
from telethon.tl.types import ChannelParticipantsAdmins
import os
os.system("clear")
print ("""

   *                     (                   )                       )  
 (  `     (      (       )\ )   (     (   ( /(   *   )            ( /(  
 )\))(    )\     )\ )   (()/(   )\  ( )\  )\())` )  /(        (   )\()) 
((_)()\((((_)(  (()/(    /(_))(((_) )((_)((_)\  ( )(_))___    )\ ((_)\  
(_()((_))\ _ )\  /(_))_ (_))  )\___((_)_   ((_)(_(_())|___|_ ((_) _((_) 
|  \/  |(_)_\(_)(_)) __||_ _|((/ __|| _ ) / _ \|_   _|    | | | ||_  /  
| |\/| | / _ \    | (_ | | |  | (__ | _ \| (_) | | |      | |_| | / /   
|_|  |_|/_/ \_\    \___||___|  \___||___/ \___/  |_|       \___/ /___|  
                                                                        

""")
#part1
import handlers.client, handlers.greetings, handlers.alive, handlers.nedoquote, handlers.quote, handlers.mquote, handlers.help, handlers.chatinfo, handlers.magicrun, handlers.nikal, handlers.lulrun, handlers.kissrun, handlers.whyrun	, handlers.uzbrun, handlers.count, handlers.type, handlers.tagall, handlers.rev, handlers.ahelp, handlers.dinorun, handlers.loverun, handlers.ketdim, handlers.policerun, handlers.fuckrun, handlers.what, handlers.brainrun, handlers.ok, handlers.yes, handlers.no, handlers.pic, handlers.pk, handlers.lovestoryrun, handlers.test, handlers.ping, handlers.admins, handlers.calcubot, handlers.b64, handlers.qrc, handlers.wm, handlers.tr, handlers.kick,handlers.wiki, handlers.loading, handlers.narutorun, handlers.sharinganrun, handlers.banall, handlers.rename
from handlers import emojify

#part2
client = handlers.client.client
#bot
botClient = handlers.client.botClient
with client as darknet:
				darknet.add_event_handler(handlers.greetings.greeting)
				
#alive
with client as darknet:
				darknet.add_event_handler(handlers.alive.alive)
				
#NedoQuote
with client as darknet:
				darknet.add_event_handler(handlers.nedoquote.nqhandler)
#quote
with client as darknet:
				darknet.add_event_handler(handlers.quote.quotehandler2)
#mquote
with client as darknet:
				darknet.add_event_handler(handlers.mquote.quotehandler3)
#help
with client as darknet:
				darknet.add_event_handler(handlers.help.helphandler)

#chatinfo
with client as darknet:
				darknet.add_event_handler(handlers.chatinfo.info)
#magic
with client as darknet:
				darknet.add_event_handler(handlers.magicrun.magichandler)
#nikal
with client as darknet:
				darknet.add_event_handler(handlers.nikal.nikalhandler)
#lul
with client as darknet:
				darknet.add_event_handler(handlers.lulrun.lulhandlers)
#kiss
with client as darknet:
				darknet.add_event_handler(handlers.kissrun.kisshandlers)
#why
with client as darknet:
				darknet.add_event_handler(handlers.whyrun.whyhandlers)
#uzb
with client as darknet:
				darknet.add_event_handler(handlers.uzbrun.uzbhandlers)
#count 
with client as darknet:
				darknet.add_event_handler(handlers.count.count)
#type
with client as darknet:
				darknet.add_event_handler(handlers.type.type)
#tagall
with client as darknet:
				darknet.add_event_handler(handlers.tagall.tagall)
				
#net yuq ligida tayorlanganlar
#					rev
with client as darknet:
				darknet.add_event_handler(handlers.rev.reverseHandler)
#ahelp
with client as darknet:
				darknet.add_event_handler(handlers.ahelp.ahelphandler)
#dino
with client as darknet:
				darknet.add_event_handler(handlers.dinorun.dinohandlers)
#love
with client as darknet:
				darknet.add_event_handler(handlers.loverun.lovehandlers)
#ketdim
with client as darknet:
				darknet.add_event_handler(handlers.ketdim.ketdihandlers)
#police
with client as darknet:
				darknet.add_event_handler(handlers.policerun.policehandlers)
#fuck
with client as darknet:
				darknet.add_event_handler(handlers.fuckrun.fuckhandlers)
#what
with client as darknet:
				darknet.add_event_handler(handlers.what.whathandlers)
#brain
with client as darknet:
				darknet.add_event_handler(handlers.brainrun.brainhandler)
#yes
with client as darknet:
				darknet.add_event_handler(handlers.yes.yeshandlers)
#ok
with client as darknet:
				darknet.add_event_handler(handlers.ok.okhandlers)
#no
with client as darknet:
				darknet.add_event_handler(handlers.no.nohandlers)
#picer
with client as darknet:
				darknet.add_event_handler(handlers.pic.picer)
#pc
with client as darknet:
				darknet.add_event_handler(handlers.pk.pkhandler)
#lovestory
with client as darknet:
				darknet.add_event_handler(handlers.lovestoryrun.lovestoryhandler)
#test
with client as darknet:
				darknet.add_event_handler(handlers.test.infoconv)
#ping
with client as darknet:
				darknet.add_event_handler(handlers.ping.pingHandler)
#admins
with client as darknet:
				darknet.add_event_handler(handlers.admins.admins)
#calc
with client as darknet:
				darknet.add_event_handler(handlers.calcubot.calcubot)
#translator
with client as darknet:
				darknet.add_event_handler(handlers.b64.runb64)
				#qrx
with client as darknet:
				darknet.add_event_handler(handlers.qrc.runqrc)
				#wm
with client as darknet:
				darknet.add_event_handler(handlers.wm.runwm)
				#tr
with client as darknet:
				darknet.add_event_handler(handlers.tr.runccr)
				#wiki
with client as darknet:
				darknet.add_event_handler(handlers.wiki.wiki)
#kick
with client as darknet:
				darknet.add_event_handler(handlers.kick.runkick)

#loading
with client as darknet:
				darknet.add_event_handler(handlers.loading.loading)
#naruto
with client as darknet:
				darknet.add_event_handler(handlers.narutorun.narutohandler)
#sharingan
with client as darknet:
				darknet.add_event_handler(handlers.sharinganrun.sharinganhandler)
#banall				
with client as darknet:
				darknet.add_event_handler(handlers.banall.runfba)
#rename
with client as darknet:
				darknet.add_event_handler(handlers.rename.rename)
#spamm
@client.on(events.NewMessage(pattern=".spam ?(.*)"))
async def delayspammer(e):
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit(f"**ishlatish :** {HNDLR}spam <dark time> <count> <msg>")
    await e.delete()
    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(dark)
    except Exception as u:
        await e.respond(f"**Hatolik :** `{u}`")
        
#emojify
@client.on(events.NewMessage(pattern=".emoji(?: |$)(.*)"))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(
            event, "Matn bn yozing..."
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.oofman:
            char = emojify.offman[emojify.oofman.index(a)]
            result += char
        else:
            result += a
    await event.edit(result)
    
#wikipedia
@client.on(events.NewMessage(pattern=".wiki ?(.*)"))
async def wiki(e):
    srch = e.pattern_match.group(1)
    if not srch:
        return await e.edit("`wikipedia qidirish uchun text kiriting !`")
    msg = await e.edit(f"`qidirilmoqda {srch} wikipedia..`")
    try:
        mk = wikipedia.summary(srch)
        te = f"**Qidiruv sorovi :** {srch}\n\n**Natija :** {mk}"
        await msg.edit(te)
    except Exception as err:
        await msg.edit(f"**ERROR** : {str(err)}")

        #manga
@client.on(events.NewMessage(pattern=".manga ?(.*)"))
async def manga(event):
    msg = await event.edit("`qidirilmoqda ...`")
    keyword = event.pattern_match.group(1)
    if keyword is None:
        return await msg.edit("`qidirish uchun anime nomini yozing`")
    try:
        animes = await event.client.inline_query("animedb_bot", f"<m> {keyword}")
        await animes[0].click(
            event.chat_id,
            reply_to=ult.reply_to_msg_id,
            silent=True if ult.is_reply else False,
            hide_via=True,
        )
        return await msg.delete()
    except Exception:
        return await msg.edit("`Topilmadi ...`")        
        







loop = asyncio.get_event_loop()
client.start()
botClient.start()
loop.run_forever()

