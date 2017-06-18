"""
Overview
========

Tells the bot to tell something to someone.

Commands
========

Command: @tell person note
Description: Instructs the bot to send a note to person.

"""

from quickirc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import command

def install(server):
    xmap(server, 'CMSG', send)
    xmap(server, 'PMSG', send)

@command('@tell person note')
def send(server, nick, user, host, target, msg, person, note):
        send_msg(server, person, note)











