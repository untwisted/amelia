"""
    This subprotocol is used to keep track of nick changes and
    house myaddr variable which contains our local ip.
"""

from untwisted.plugins.irc import send_cmd
from untwisted.network import hold, xmap

def install(server):
    xmap(server, '376', _376)
    xmap(server, 'NICK', nick)

def _376(server, servaddr, nick, msg):
    server.nick = nick
    send_cmd(server, 'USERHOST %s' % nick)
    
    _, args = yield hold(server, '302')
    _, _, _, ident = args
    user, myaddr = ident.split('@')

    server.myaddr  = myaddr

def nick(server, nick_x, user, host, nick_y):
    if server.nick == nick_x:
        server.nick = nick_y



