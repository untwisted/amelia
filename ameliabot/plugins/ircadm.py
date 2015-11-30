from ameliabot.adm import is_adm
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg

def install(server, *args):
    xmap(server, ('CMSG', '.irc_cmd'), irc_cmd)

def irc_cmd(server, (nick, user, host, target, msg,), *args):
    if is_adm(host): send_cmd(server, ' '.join(args))




