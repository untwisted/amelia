""" 
Author:Iury O. G. Figueiredo
Name:codebox
Description: This plugin uses codepage.org to run code.
Usage:

<Tau>.run python print [ind for ind in range(20) if ind % 2]
<yu> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
<Tau>.run c int main(void) { printf("Hello World\n"); return 0; }
<yu> Hello World
"""

from ameliabot.utils import codepad
from untwisted.plugins.irc import send_msg
from untwisted.network import xmap

class Codebox(object):
    def __init__(self, server, max_width=512 * 3):
        self.max_width = max_width
        xmap(server, ('PRIVCHAN', '.run'), self.run)

    def run(self, server, (nick, user, host, target, msg), lang, *args):
        code = ' '.join(args)

        url, output = codepad.sandbox(code, lang)

        if len(output) <= self.max_width:
            send_msg(server, target, output)
        else:
            send_msg(server, target, url)




