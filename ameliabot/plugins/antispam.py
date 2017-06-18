"""
Usage: 

# ./amelia/ameliarc

from ameliabot.plugins import antispam

def PLUGIN_SCHEME(server):
    # 1 lines per second, command to be executed if the rate is overriden.
    antispam.install(server, n_lines, n_secs,  cmd='kick {chan} {nick} :Amelia rocks!')

"""

from quickirc import send_cmd, send_msg
from untwisted.network import xmap
from ameliabot.cmd import regcmd
import time

class AntiSpam(object):
    def __init__(self, server, n_lines, n_secs, cmd):
        """
        The n_lines means the number of lines per n_secs.

        Example for command:
            cmd = 'kick {chan} {nick} :Amelia rocks!'
            cmd = 'chanserv akick {chan} add *!*@{host} : get out!
        """
        xmap(server, 'CMSG', self.watcher)
        self.data    = {}
        self.n_lines = n_lines
        self.n_secs  = n_secs
        self.cmd     = cmd

    def watcher(self, server, nick, user, host, target, msg):
        count, start       = self.data.setdefault(host, [0,  time.time()])
        count              = count + 1
        self.data[host][0] = count

        if time.time() - start > self.n_secs:
            self.data[host][0], self.data[host][1] = 0, time.time()
            if self.n_lines/float(self.n_secs) < count/(time.time() - start):
                send_cmd(server, self.cmd.format(nick=nick, 
                         chan=target, host=host, user=user))

install = AntiSpam













