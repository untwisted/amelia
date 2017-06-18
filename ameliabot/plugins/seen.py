""" 
Overview
========

Used to check last time a peer was seen online.

Commands
========

Command: @seen peer
Description: Show how long a nick has been inactive.

"""

from quickirc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import command
import time

class Seen(object):
    def __init__(self, server):
        self.database = dict()

        xmap(server, 'CMSG', self.record)
        xmap(server, 'CMSG', self.check)

    def record(self, server, nick, user, host, target, msg):
        self.database[nick.lower()] = time.time()

    @command('@seen peer')
    def check(self, server, nick, user, host, target, msg, peer):
        try:
            initial = self.database[peer.lower()] 
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
                '%s last seen %s:%s:%s ago.' % (peer, hour, min, sec))



install = Seen


