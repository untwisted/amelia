"""
"""

from random import choice
from gsearch import GSearch
from untwisted.plugins.irc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import command

class QuickSearch(object):
    def __init__(self, server):
        self.gsearch = GSearch()
        xmap(server, 'CMSG', self.find)
    
    @command('@find data')
    def find(self, server, nick, user, host, target, msg, data):
        result = self.gsearch.quick_search(v='0.1', q=data, safe='high')
        send_msg(server, target, str(choice(result)))
    
install = QuickSearch






