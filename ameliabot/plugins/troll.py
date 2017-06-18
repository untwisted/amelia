"""
Overview
========

Whenever it matches a combination of letters that appear to be a laught
it makes the bot laught as well.
"""

from quickirc import send_msg
from re import search, compile
from random import choice, randint
from untwisted.network import xmap

class Troll(object):
    def __init__(self, server, letters, min, max):
        self.letters = letters
        self.max     = max
        self.min     = min
        self.pattern = compile('[%s]{%s,%s}' % (letters, min, max))
        xmap(server, 'CMSG', self.check_msg)

    def check_msg(self, server, nick, user, host, target, msg):
        if search(self.pattern, msg): 
            send_msg(server, target, self.make_seq())
        
    def make_seq(self):
        data   = ''
        for ind in range(0, randint(self.min, self.max)):
            data = data + choice(self.letters)
        return data

install = Troll



