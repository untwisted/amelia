from untwisted.network import spawn, xmap
import re

#ARG_STR = "[^ ]+"
#This regex supports "alpha beta gama" parameters between ""
ARG_STR = '[^" ]+|"[^"]+"'
ARG_REG = re.compile(ARG_STR)

def install(server):
    xmap(server, 'PRIVMSG', split)

def split(server, *args):
    """ The PRIVCHAN sign conveys
        (server, nick, user, host, target, msg, source)
        as args. This is useful when you want to link
        a callback to be called whenever a privmsg is issued
        be it sent to user or channel.
        The source would be the nick when it is to is sent to you
        and a chan when it is sent to a channel.
    """
    if args[3].startswith('#'):
        spawn(server, 'PRIVCHAN', *args)
    else:
        spawn(server, 'PRIVUSER', *args)
        
