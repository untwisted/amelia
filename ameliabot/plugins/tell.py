from untwisted.plugins.irc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import command

def install(server):
    xmap(server, 'CMSG', send)
    xmap(server, 'PMSG', send)

@command('@tell person note')
def send(server, nick, user, host, target, msg, person, note):
        send_msg(server, person, note)









