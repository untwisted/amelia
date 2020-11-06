""" 
Overview
========

This plugin implements a mechanism to execute code on codepad using a sophisticated approach.
It uses a scheme of cmds like #py to start a sequence of code and #end to close. It supports
other langs like c, haskell etc.

Example
=======

<\tau> =py
<\tau> def calc():
<\tau> 	print 'hello world'
<\tau> calc()
<\tau> =end
<\amelia>  hello world

<\tau> =c
<\tau> int main(int argv, char *argv[]) {
<\tau> 	printf("hello world");
<\tau> 	return 0;
<\tau> }
<\tau> =end
<\amelia> : error: conflicting types for 'argv' : error: previous definition of 'argv' was here

"""

from quickirc import send_msg
from untwisted.tools import coroutine
from pytio import TioRequest
from ameliabot.plugins.codebox import tio

class Codenv:
    def __init__(self, server, lang, start_cmd, end_cmd, max_length=512 * 3):
        self.lang = lang
        self.max_length = max_length
        self.start_cmd = start_cmd
        self.end_cmd   = end_cmd
        server.add_map('CMSG', self.check_msgcmd)

    @coroutine
    def accumulate_code(self, server, nick, user, host, target, msg):
        code = ''
        while True:
            args = yield server, 'CMSG'
            if args[3] == target and args[2] == host:
                if args[4] != self.end_cmd:
                    code = code + args[4] + '\n'
                else:
                    break

        request = TioRequest(lang=self.lang, code=code)
        response = tio.send(request)
        send_msg(server, target, response.result[:self.max_length])

    def check_msgcmd(self, *args):
        if args[-1]  == self.start_cmd: 
            return self.accumulate_code(*args)


install = Codenv

