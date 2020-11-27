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

from pytio import Tio, TioRequest
from quickirc import send_msg
from ameliabot.cmd import regcmd

tio = Tio()
class Codebox(object):
    def __init__(self, server, max_length=512 * 3):
        self.max_length = max_length
        server.add_map('CMSG', self.run)

    @regcmd('@run (?P<lang>[^ ]+) (?P<code>.+)')
    def run(self, server, nick, user, host, target, msg, lang, code):
        request = TioRequest(lang=lang, code=code)
        response = tio.send(request)
        print('code:', code)
        send_msg(server, target, response.result[:self.max_length])


install = Codebox







