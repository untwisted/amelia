"""
Overview
========
This plugin uses wolfram alpha to compute mathematical expressions.

Commands
========

Command: @calc expression
Description: Computes the expression using wolfram alpha.

Example
=======

<\tau> @calc integrate x^2
<\amelia>  integral x^2  dx = x^3/3+constant

"""

import wolframalpha

from untwisted.plugins.irc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import regcmd

class Calculate(object):
    def __init__(self, server, appid):
        self.client = wolframalpha.Client(appid)
        xmap(server, 'CMSG', self.calculate)
    
    @regcmd('@calc (?P<exp>.+)$')
    def calculate(self, server, nick, user, host, target, msg, exp):
        req = self.client.query(exp)
        send_msg(server, target, req.results.next().text)
    
install = Calculate














