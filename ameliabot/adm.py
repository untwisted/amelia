from untwisted.network import xmap
from quickirc import send_msg
from ameliabot.cmd import command

known = set()

def install(server):
    xmap(server, 'PMSG', login)

@command('@login password')
def login(server, nick, user, host, target, msg, password):
    if password == server.adm_passwd:
        known.add(host)
        send_msg(server, nick, 'Logged!')
    else:
        send_msg(server, nick, 'Invalid password!')

def is_adm(host):
    return host in known






