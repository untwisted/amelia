""" 
Author:Iury O. G. Figueiredo
Name:codenv
Description: This plugin uses codepage.org to run code.
Usage:
<Tau>@run python
<Tau>print 'alpha'
<Tau>@end
<ameliabot> alpha

"""

from ameliabot.utils import codepad
from untwisted.plugins.irc import send_msg
from untwisted.network import hold, xmap

class Codenv(object):
    def __init__(self, server, start_tag, end_tag, max_width=512 * 3):
        self.max_width = max_width
        self.start_tag = start_tag
        self.end_tag   = end_tag

        xmap(server, ('PRIVCHAN', self.start_tag), self.proc)

    def proc(self, server, (nick, user, host, target, msg), lang):
        code = ''
        flag = hold(server, 'PRIVCHAN')
        while True:
            event, args = yield flag 
            if args[4] == target and args[3] == host:
                if args[5] == self.end_tag:
                    break
                code = code + args[5] + '\n'
            
        url, output = codepad.sandbox(code, lang)

        if len(output) <= self.max_width:
            send_msg(server, target, output)
        else:
            send_msg(server, target, url)


install = Codenv



