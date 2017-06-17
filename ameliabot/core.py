from untwisted.network import Spin, xmap
from untwisted.iostd import Client, Stdin, Stdout, CLOSE, CONNECT_ERR, CONNECT
from untwisted.splits import Terminator, logcon
from quickirc import Irc, CTCP, Misc, send_cmd
from socket import socket, AF_INET, SOCK_STREAM, socket, gethostbyname
from ameliabot import adm
from untwisted.tools import coroutine

def connect(servaddr, port, nick, user, nick_passwd, adm_passwd, chan_list):
    sock   = socket(AF_INET, SOCK_STREAM)
    ip     = gethostbyname(servaddr)
    server = Spin(sock)
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
        Stdin(server)
        Stdout(server)
        Terminator(server)

        Irc(server)
        CTCP(server)

        Misc(server)
        adm.install(server)

        xmap(server, 'PING', lambda server, prefix, servaddr: 
                send_cmd(server, 'PONG :%s' % servaddr))
        
        xmap(server, CLOSE, lambda server, err: lose(server))
        logcon(server)

        xmap(server, '376', auto_join)
        xmap(server, '376', get_myaddr)
        xmap(server, 'NICK', update_nick)

        server.servaddr    = servaddr
        server.port        = port
        server.nick        = nick
        server.user        = user
        server.chan_list   = chan_list
        server.nick_passwd = nick_passwd
        server.adm_passwd  = adm_passwd

        send_cmd(server, 'NICK %s' % nick)
        send_cmd(server, 'USER %s' % user) 
    
    xmap(server, CONNECT, handle_connect)
    xmap(server, CONNECT_ERR, lambda server, err: lose(server))

    server.connect_ex((ip, port))
    return server






