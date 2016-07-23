"""
Usage: 

# ./amelia/ameliarc

from ameliabot.plugins import antispam

def PLUGIN_SCHEME(server):
    # 1 lines per second, command to be executed if the rate is overriden.
    antispam.install(server, rate=1,  cmd='kick {chan} {nick} :Amelia rocks!')

"""

from untwisted.plugins.irc import send_cmd, send_msg
from untwisted.network import xmap
from ameliabot.cmd import regcmd
import time

class AntiSpam(object):
    def __init__(self, server, rate=1, cmd='kick {chan} {nick} :Amelia rocks!'):
        """
        Example for rate:
            rate = lines/second.

        Example for command:
            cmd = 'kick {chan} {nick} :Amelia rocks!'
            cmd = 'chanserv akick {chan} add *!*@{host} : get out!
        """
        xmap(server, 'CMSG', self.watcher)
        self.data = {}
        self.rate = rate
        self.cmd  = cmd
        self.MAX  = 2

    def watcher(self, server, nick, user, host, target, msg):
        count, start       = self.data.setdefault(host, [0,  time.time()])
        count              = count + 1
        self.data[host][0] = count

        if self.rate < count/(time.time() - start):
            send_cmd(server, self.cmd.format(nick=nick, chan=target, host=host, user=user))

        if time.time() - start > self.MAX:
            self.data[host][0], self.data[host][1] = 0, time.time()

install = AntiSpam










