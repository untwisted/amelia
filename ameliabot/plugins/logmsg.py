"""
Author: Iury O. G. Figueiredo.
Name: logmsg
Description: Once it is loaded all channel and private msgs are logged into a file.

Example.

#coffee
#c
amelia

Where those are file names.
So, whenever somebody types on #coffee it will be appended
to #coffee file.
"""

from uxirc.misc import *
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
        xmap(server, 'PRIVCHAN', self.store_chan)
        xmap(server, 'PRIVUSER', self.store_user)

    def store_chan(self, server, nick, user, host, target, msg):
        with open('%s/%s' % (self.folder, target), 'a+') as fd:
            fd.write('(%s)<%s> %s\n' % (asctime(), nick, msg))

    def store_user(self, server, nick, user, host, target, msg):
        with open('%s/%s' % (self.folder, nick), 'a+') as fd:
            fd.write('(%s)<%s> %s\n' % (asctime(), nick, msg))

