"""
Author: Iury O. G. Figueiredo.
Name: laugh
Description: It laughts whenever one laughts.
Usage:

<Tau>ahuehae
<yu>uiho
<Tau>aheuhaeuhae
<yu>ioaiuohea
"""

from untwisted.plugins.irc import send_msg
from re import search, compile
from random import choice, randint
from untwisted.network import xmap

LETTER_TUPLE = ('a', 'e', 'h', 'i', 'o', 'u')
MAX_LENGTH = 16
MIN_LENGTH = 4
LAUGH_STR = '[haeiou]{7,}'
LAUGH_REG = compile(LAUGH_STR)

def install(server):
    xmap(server, 'PRIVCHAN', track_laugh)

def track_laugh(server, nick, user, host, target, msg):
    if not search(LAUGH_REG, msg): return

    length = randint(MIN_LENGTH, MAX_LENGTH)
    data   = ''

    for ind in range(0, length):
        data = data + choice(LETTER_TUPLE)
    send_msg(server, target, data)


