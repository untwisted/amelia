""" 
Overview
========

This plugin implements a mechanism to execute code on codepad using a sophisticated approach.
It uses a scheme of tags like #py to start a sequence of code and #end to close. It supports
other langs like c, haskell etc.

Example
=======

<\tau> #py
<\tau> def calc():
<\tau> 	print 'hello world'
<\tau> calc()
<\tau> #end
<\amelia>  hello world

<\tau> @c
<\tau> int main(int argv, char *argv[]) {
<\tau> 	printf("hello world");
<\tau> 	return 0;
<\tau> }
<\tau> @end
<\amelia> : error: conflicting types for 'argv' : error: previous definition of 'argv' was here

"""

import libpad
from untwisted.plugins.irc import send_msg
from untwisted.network import hold, xmap

class Codenv(object):
    def __init__(self, server, lang, start_tag, end_tag, max_width=512 * 3):
        self.lang = lang
        self.max_width = max_width
        self.start_tag = start_tag
        self.end_tag   = end_tag
        xmap(server, 'CMSG', self.process)

    def process(self, server, nick, user, host, target, msg):
        if not msg == self.start_tag: return
        code = ''
        flag = hold(server, 'CMSG')

        while True:
            event, args = yield flag 
            if args[4] == target and args[3] == host:
                if args[5] == self.end_tag:
                    break
                code = code + args[5] + '\n'
            
        url, output = libpad.sandbox(code, self.lang)
        if len(output) <= self.max_width:
            send_msg(server, target, output)
        else:
            send_msg(server, target, url)

install = Codenv








