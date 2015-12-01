""" 
"""

import libpad
from untwisted.plugins.irc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import command

class Codebox(object):
    def __init__(self, server, max_width=512 * 3):
        self.max_width = max_width
        xmap(server, 'CMSG', self.run)

    @command('@run -l lang -c code')
    def run(self, server, nick, user, host, target, msg, lang, code):
        url, output = libpad.sandbox(code, lang)

        if len(output) <= self.max_width:
            send_msg(server, target, output)
        else:
            send_msg(server, target, url)


install = Codebox
