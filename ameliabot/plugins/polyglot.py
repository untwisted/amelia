"""
"""

from untwisted.network import spawn, xmap, zmap
from gdict import GoogleTranslator, shape
from untwisted.plugins.irc import send_msg
from ameliabot.cmd import command

source = GoogleTranslator()

def install(server):
    xmap(server, 'CMSG', split)
    xmap(server, 'CMSG', add)
    xmap(server, 'CMSG', rm)

@command('@polyglot-add lang_x lang_y ident')
def add(server, nick, user, host, target, 
               msg, lang_x, lang_y, ident):
    xmap(server, ident, listen, lang_x, lang_y)

@command('@polyglot-del lang_x lang_y ident')
def rm(server, nick, user, host, target, 
               msg, lang_x, lang_y, ident):
    zmap(server, ident, listen, lang_x, lang_y)

def listen(server, nick, user, target, msg, lang_x, lang_y):
    data = source.translate(msg, lang_x, lang_y) 
    data = shape(data)
    send_msg(server, target, '%s %s' % (nick, data))

def split(server, nick, user, host, target, msg):
    spawn(server, host, nick, user, target, msg)








