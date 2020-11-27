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
from ameliabot.cmd import command

def install(server):
    server.add_map('CMSG', send)
    server.add_map('PMSG', send)

@command('@tell person note')
def send(server, nick, user, host, target, msg, person, note):
        send_msg(server, person, note)











