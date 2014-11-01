""" 
Author:Iury O. G. Figueiredo
Name:codenv
Description: This plugin uses codepage.org to run code.
Usage:
<Tau>.proc python .done
<Tau>def snard(value):
<Tau>    for ind in range(value):
<Tau>        print 'snardbafulator is a molester'
<Tau>snard(6)
<Tau>.done
<yu> snardbafulator is a molester snardbafulator is a molester snardbafulator is a molester snardbafulator is a molester snardbafulator is a molester snardbafulator is a molester

"""

from ameliabot.utils import codepad
from uxirc.misc import *
from untwisted.network import hold, xmap

class Codenv(object):
    def __init__(self, server, max_width=512 * 3):
        self.max_width = max_width
        xmap(server, ('PRIVCHAN', '.$'), self.proc)

    def proc(self, server, (nick, user, host, target, msg), lang, tag):
        code = ''
        flag = hold(server, 'PRIVCHAN')
        while True:
            event, args = yield flag 
            if args[4] == target and args[3] == host:
                if args[5] == tag:
                    break
                code = code + args[5] + '\n'
            
        url, output = codepad.sandbox(code, lang)

        if len(output) <= self.max_width:
            send_msg(server, target, output)
        else:
            send_msg(server, target, url)



