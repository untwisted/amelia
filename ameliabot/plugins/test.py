from untwisted.network import xmap
from untwisted.plugins.irc import send_msg

def install(server):
    xmap(server, ('PRIVCHAN', '.test'), test)
    xmap(server, ('PRIVCHAN', '.chnick'), chnick)

def test(server, (nick, user, 
                host, target, msg,), ):

    print 'myaddr:', server.myaddr, 'nick:', server.nick, 'servaddr', 
        server.servaddr, 'user:', server.user

def chnick(server, (nick, user, 
                host, target, msg), new_nick):
    send_cmd(server, 'NICK %s' % new_nick)



