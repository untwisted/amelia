"""
Overview
========

Generate latex from basic python expressions.
Meant to be used in ##math at irc.freenode.org

Commands
========

Command: @lax expression
Description: Output latex for the expression.

Example
=======


"""


from quickirc import send_msg
from ameliabot.cmd import regcmd
from ameliabot.tools import send_lines
from liblax.parser import run

class LatexBuilder(object):
    def __init__(self, server):
        server.add_map('CMSG', self.build)
    
    @regcmd('@lax (?P<exp>.+)$')
    def build(self, server, nick, user, 
                    host, target, msg, exp):

        try:
            data = str(run(exp))
        except Exception as e:
            send_lines(server, target, str(e))
        else:
            send_lines(server, target, data)
      
install = LatexBuilder













