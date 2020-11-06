"""
"""

from random import choice
from re import split
from os.path import dirname, join
from quickirc import send_msg
from ameliabot.cmd import command

class Quote(object):
    def __init__(self, server):
        fd   = open(join(dirname(__file__), 'quote_database'), 'rb')
        data = fd.read().decode('utf8', 'ignore')
        fd.close()
        self.data = split('\n+', data)
        
        server.add_map('CMSG', self.send_quote)

    @command('@quote')
    def send_quote(self, server, nick, user, host, target, msg):    
        quote = choice(self.data)
        send_msg(server, target, quote)
    
install = Quote










