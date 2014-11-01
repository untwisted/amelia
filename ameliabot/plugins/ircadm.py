from uxirc.misc import *
from ameliabot.adm import is_adm
from untwisted.network import xmap

def install(server, *args):
    xmap(server, ('PRIVCHAN', '.irc_cmd'), irc_cmd)

def irc_cmd(
            server, 
            (
                nick, user, 
                host, target, 
                msg,
            ),
            *args
           ):
    
    if is_adm(host):
        send_cmd(server, ' '.join(args))

