"""
Overview
========

Used to extract url titles from links.

"""

from untwisted.plugins.irc import send_msg
from ameliabot.utils.title import Title
from re import search, compile, sub
from untwisted.network import xmap

STR_LINK  = '(?P<address>http[s]?://[^ ]*)'
REG_LINK  = compile(STR_LINK)
STR_BLANK = r'\s+'
REG_BLANK = compile(STR_BLANK)

class UrlTitle(object):
    def __init__(self, server):
        self.title = Title()
        xmap(server, 'CMSG', self.check)
    
    def check(self, server, nick, user, host, target, msg):
        struct = search(REG_LINK, msg)
        if not struct: 
            return
        page_title = self.title.get_title(struct.group('address'))
        page_title = sub(REG_BLANK, ' ', page_title) 
        send_msg(server, target, page_title)

install = UrlTitle


