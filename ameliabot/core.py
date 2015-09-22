from untwisted.network import Spin, xmap
from untwisted.utils.stdio import *
from untwisted.utils.shrug import *
from untwisted.plugins.irc import *
from socket import socket, AF_INET, SOCK_STREAM
from ameliabot import adm
from ameliabot import cmd
from ameliabot import profile
from ameliabot import priv

def connect(servaddr, port, nick, user, nick_passwd, adm_passwd, chan_list, plugmap):
    sock = socket(AF_INET, SOCK_STREAM)
    ip = gethostbyname(servaddr)
    server = Spin(sock)
    Client(server)

    def auto_join(server, *args):
        send_msg(server, 'nickserv', 'identify %s' % nick_passwd)
        for ind in chan_list:
            send_cmd(server, 'JOIN %s' % ind)

   
    def handle_connect(server):
        Stdin(server)
        Stdout(server)
        Shrug(server)

        Irc(server)
        CTCP(server)
        priv.install(server)
        cmd.install(server)
        profile.install(server)
        adm.install(server)

        xmap(server, 'PING', lambda server, prefix, servaddr: 
                send_cmd(server, 'PONG :%s' % servaddr))
        
        xmap(server, CLOSE, lambda server, err: lose(server))
        logcon(server)

        xmap(server, '376', auto_join)

        plugmap(server)

        server.servaddr = servaddr
        server.port = port
        server.nick = nick
        server.user = user
        server.chan_list = chan_list
        server.nick_passwd = nick_passwd
        server.adm_passwd = adm_passwd
        server.plugmap = plugmap


        send_cmd(server, 'NICK %s' % nick)
        send_cmd(server, 'USER %s' % user) 
    
    xmap(server, CONNECT, handle_connect)
    xmap(server, CONNECT_ERR, lambda server, err: lose(server))

    server.connect_ex((ip, port))

    return server


