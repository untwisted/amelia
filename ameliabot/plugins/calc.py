"""
"""

from ameliabot.utils.mathapi import MathApi
from untwisted.plugins.irc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import regcmd

class Calculate(object):
    def __init__(self, server, appid):
        self.source = MathApi(appid)
        xmap(server, 'CMSG', self.calculate)
    
    @regcmd('@calc (?P<exp>.+)$')
    def calculate(self, server, nick, user, host, target, msg, exp):
        send_msg(server, target, self.source.submit(exp))
    
install = Calculate








