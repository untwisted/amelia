"""
Overview
========

Used to log msgs into a folder.

"""

from time import asctime
from untwisted.network import xmap

class LogMsg(object):
    def __init__(self, server, folder):
        """
        The folder is where to save the logs.
        Example:
        LogMsg(server, '/home/tau')

        Notice it shouldn't be '/home/tau/'.
        """

        self.folder = folder
        xmap(server, 'CMSG', self.store_chan)
        xmap(server, 'PMSG', self.store_user)

    def store_chan(self, server, nick, user, host, target, msg):
        with open('%s/%s' % (self.folder, target), 'a+') as fd:
            fd.write('(%s)<%s> %s\n' % (asctime(), nick, msg))

    def store_user(self, server, nick, user, host, target, msg):
        with open('%s/%s' % (self.folder, nick), 'a+') as fd:
            fd.write('(%s)<%s> %s\n' % (asctime(), nick, msg))





