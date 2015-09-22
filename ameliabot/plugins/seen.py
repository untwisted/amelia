""" 
Author: Iury O. G. Figueiredo.
Name: seen
Description: Used to see the last time a nick was seen.
Usage:

<Tau>.seen sailorreality
<yu>sailorreality last seen 10:58:27 ago.

It saves the last time the person joined a channel where the bot is in.
"""
from untwisted.plugins.irc import send_msg
from untwisted.network import xmap
import time

class Seen(object):
    def __init__(self, server):
        self.database = dict()

        xmap(server, 'PRIVMSG', self.record)
        xmap(server, ('PRIVCHAN', '.seen'), self.check)

    def record(self, server, nick, user, host, target, msg):
        self.database[nick.upper()] = time.time()

    def check(self, server, (nick, user, host, target, msg), one):
        try:
            initial = self.database[one.upper()] 
        except:
            send_msg(server, target, "No records for that nick.")
        else:
            final   = time.time()
            rate    = final - initial
            hour    = int(rate / (60 ** 2))
            rate    = int(rate % (60 ** 2))
            min     = int(rate / 60)
            sec     = int(rate % 60)

            send_msg(server, target, 
                '%s last seen %s:%s:%s ago.' % (one, hour, min, sec))





