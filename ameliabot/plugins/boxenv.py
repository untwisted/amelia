""" 
Author:Iury O. G. Figueiredo
Name:codenv
Description: This plugin uses codepage.org to run code.
Usage:

"""

from ameliabot.utils import codepad
from ameliabot.utils.tools import send_lines
from untwisted.network import hold, xmap

class BoxEnv(object):
    def __init__(self, server, lang, start_tag,
                       sep_tag, end_tag, 
                       max_width=512 * 3):

        self.lang = lang
        self.sep_tag = sep_tag
        self.start_tag = start_tag
        self.end_tag = end_tag
        self.max_width = max_width
        xmap(server, ('PRIVCHAN', self.start_tag), self.proc)

    def proc(self, server, (nick, user, host, target, msg)):
        code = []
        flag = hold(server, 'PRIVCHAN')
        while True:
            event, args = yield flag 
            if args[4] == target and args[3] == host:
                if args[5].startswith(self.end_tag): 
                    break

                if args[5].startswith(self.sep_tag): 
                    code.append('%s' % args[5].lstrip(self.sep_tag))
            
        url, output = codepad.sandbox('\n'.join(code), self.lang)
        if len(output) <= self.max_width:
        # So, i don't have the newlines removed.
            send_lines(server, target, output)
        else:
            send_msg(server, target, url)








