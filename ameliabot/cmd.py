from untwisted.network import spawn, xmap
from re import compile, findall

ARG_STR = "[^ ]+"
ARG_REG = compile(ARG_STR)

#This regex supports "alpha beta gama" parameters between ""
#ARG_STR = '[^" ]+|"[^"]+"'
#ARG_REG = re.compile(ARG_STR)

def install(server):
    xmap(server, 'PRIVCHAN', split, 'PRIVCHAN')
    xmap(server, 'PRIVUSER', split, 'PRIVUSER') 

def split(server, nick, user, host, target, msg, event):
    if msg.startswith('.') or msg.startswith('@'):
        cmdlist = findall(ARG_REG, msg)
        spawn(  
               server,
               (event, cmdlist[0]), 
               (
                 nick,
                 user, 
                 host,
                 target,
                 msg,
               ),
               *cmdlist[1:]
             )
    


