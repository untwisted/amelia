""" 
Overview
========

This plugin implements a mechanism to execute code on codepad using a sophisticated approach.
It uses a scheme of tags like #py to start a sequence of code and #end to close. It supports
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

import libpad
from quickirc import send_msg
from untwisted.network import xmap
from untwisted.tools import coroutine

class Codenv(object):
    def __init__(self, server, lang, start_tag, end_tag, max_width=512 * 3):
        self.lang = lang
        self.max_width = max_width
        self.start_tag = start_tag
        self.end_tag   = end_tag
        xmap(server, 'CMSG', self.process)

    @coroutine
    def process(self, server, nick, user, host, target, msg):
        if not msg == self.start_tag: return
        code = ''
        
        while True:
            args = yield server, 'CMSG'
            if args[3] == target and args[2] == host:
                if args[4] == self.end_tag:
                    break
                code = code + args[4] + '\n'
        url, output = libpad.sandbox(code, self.lang)
        if len(output) <= self.max_width:
            send_msg(server, target, output)
        else:
            send_msg(server, target, url)

install = Codenv












