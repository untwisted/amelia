"""
Author: Iury O. G. Figueiredo.
Name: snarf
Description: It is used to show link titles when 
they are sent over a channel.
Usage:

<Tau>http://sourceforge.net/p/ameliabot/code/ci/bfc349208e26ca29cabce15f1613ca6780fb4f9f/tree/
<yu> ameliabot / Code / [bfc349]

"""
from untwisted.plugins.irc import send_msg
from ameliabot.utils.title import Title
from re import search, compile, sub
from untwisted.network import xmap

source = Title()

STR_LINK = '(?P<address>http[s]?://[^ ]*)'
REG_LINK = compile(STR_LINK)

STR_BLANK = r'\s+'
REG_BLANK = compile(STR_BLANK)

def install(server):
    xmap(server, 'PRIVCHAN', track_title)

def track_title(server, nick, user, host, target, msg):
    rex = search(REG_LINK, msg)
    if not rex: return

    url        = rex.group('address')
    page_title = source.get_title(url)
    page_title = sub(REG_BLANK, ' ', page_title) 
    send_msg(server, target, page_title)







