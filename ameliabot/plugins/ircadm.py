from ameliabot.adm import is_adm
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg
from ameliabot.cmd import command

def install(server, *args):
    xmap(server, 'CMSG', irc_cmd)

@command('@irccmd data')
def irc_cmd(server, nick, user, host, target, msg, data):
    if is_adm(host): send_cmd(server, data)





