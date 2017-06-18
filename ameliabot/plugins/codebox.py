""" 
Overview
========

This plugin uses codepad.org to run inline code and output
the result on the channel. The output is a url unless the length of the output is short enough.

Commands
========

Command: @run lang code
Description: Run inline code on codepad.org.

Example
=======
<\tau> @run python print 'hi'
<\amelia>  hi

"""

import libpad
from quickirc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import regcmd

class Codebox(object):
    def __init__(self, server, max_width=512 * 3):
        self.max_width = max_width
        xmap(server, 'CMSG', self.run)

    @regcmd('@run (?P<lang>[^ ]+) (?P<code>.+)')
    def run(self, server, nick, user, host, target, msg, lang, code):
        url, output = libpad.sandbox(code, lang)

        if len(output) <= self.max_width:
            send_msg(server, target, output)
        else:
            send_msg(server, target, url)


install = Codebox







