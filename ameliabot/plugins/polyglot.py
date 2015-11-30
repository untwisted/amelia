"""
Author: Iury O. G. Figueiredo.
Name: polyglot
Description: This plugin can be used to translate one person speech at time it is spoken on irc.
Usage:
<Tau>.polyglot_add pt en .
<yu>Tau ". polyglot_add en en 189-127-54- 128.i - next.psi.br"
<Tau>interessante.
<yu>Tau "interesting."
<Tau>agora posso falar portugues e alguem me traduz para o ingles.
<yu>Tau "now I can speak Portuguese and someone translated into English ."

If i just dont want it anymore.

<Tau>.polyglot_rm en pt 189-127-54-128.i-next.psi.br

The parameter actually is host. It is found when you do /whois on some nick.
The pt en are the google key for portuguese and english. it accepts other keys 
but you would have to figure it out.
"""

from untwisted.network import spawn, xmap, zmap
from ameliabot.utils.google import GoogleTranslator, shape
from untwisted.plugins.irc import send_msg

source = GoogleTranslator()

def install(server):
    xmap(server, 'CMSG', split)
    xmap(server, ('CMSG', '.polyglot_add'), add)
    xmap(server, ('CMSG', '.polyglot_rm'), rm)

def add(server, user, lang_x, lang_y, host):
    xmap(server, host, listen, lang_x, lang_y)

def rm(server, user, lang_x, lang_y, host):
    zmap(server, host, listen, lang_x, lang_y)

def listen(server, nick, user, target, msg, lang_x, lang_y):
    data = source.translate(msg, lang_x, lang_y) 
    data = shape(data)
    send_msg(server, target, '%s %s' % (nick, data))

def split(server, nick, user, host, target, msg):
    spawn(server, host, nick, user, target, msg)





