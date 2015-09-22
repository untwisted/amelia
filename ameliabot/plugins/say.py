from untwisted.plugins.irc import send_msg
from untwisted.network import xmap

def install(server):
    xmap(server, 'PRIVCHAN', say)

def say(server, nick, user, host, target, msg):
        send_msg(server, target, 'You said: %s' % msg)




