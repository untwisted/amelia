from untwisted.network import xmap
from untwisted.plugins.irc import send_msg

known = set()

def install(server):
    xmap(server, ('PRIVUSER', '.login'), login)
 
def login(server, (nick, user, host, target, msg, ), chunk):
    if chunk == server.adm_passwd:
        known.add(host)
        send_msg(server, nick, 'Logged.')
    else:
        send_msg(server, nick, 'Invalid password.')

def is_adm(host):
    return host in known



