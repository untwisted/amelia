from socket import socket, AF_INET, SOCK_STREAM, gethostbyname
from untwisted.network import SuperSocket
from untwisted.client import Client, lose
from untwisted.sock_writer import SockWriter
from untwisted.event import CLOSE, CONNECT_ERR, CONNECT
from untwisted.sock_reader import SockReader
from untwisted.splits import Terminator, logcon
from quickirc import Irc, CTCP, Misc, send_cmd
from ameliabot import adm
from untwisted.tools import coroutine

def connect(servaddr, port, nick, user, nick_passwd, adm_passwd, chan_list):
    sock   = socket(AF_INET, SOCK_STREAM)
    ip     = gethostbyname(servaddr)
    server = SuperSocket(sock)
    Client(server)

    def auto_join(server, *args):
        send_cmd(server, nick_passwd)
        for ind in chan_list:
            send_cmd(server, 'JOIN %s' % ind)

    @coroutine
    def get_myaddr(server, servaddr, nick, msg):
        server.nick = nick
        send_cmd(server, 'USERHOST %s' % nick)
        args        = yield server, '302'
        _, _, ident = args
        user, myaddr   = ident.split('@')
        server.myaddr  = myaddr

    def update_nick(server, nick_x, user, host, nick_y):
        if server.nick == nick_x:
            server.nick = nick_y
    
    def handle_connect(server):
        SockWriter(server)
        SockReader(server)
        Terminator(server)

        Irc(server)
        CTCP(server)

        Misc(server)
        adm.install(server)

        server.add_map('PING', lambda server, prefix, servaddr: 
        send_cmd(server, 'PONG :%s' % servaddr))
        
        server.add_map(CLOSE, lambda server, err: lose(server))
        logcon(server)

        server.add_map('376', auto_join)
        server.add_map('376', get_myaddr)
        server.add_map('NICK', update_nick)

        server.servaddr    = servaddr
        server.port        = port
        server.nick        = nick
        server.user        = user
        server.chan_list   = chan_list
        server.nick_passwd = nick_passwd
        server.adm_passwd  = adm_passwd

        send_cmd(server, 'NICK %s' % nick)
        send_cmd(server, 'USER %s' % user) 
    
    server.add_map(CONNECT, handle_connect)
    server.add_map(CONNECT_ERR, lambda server, err: lose(server))

    server.connect_ex((ip, port))
    return server






