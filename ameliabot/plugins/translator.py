"""
Overview
========

Used to translate quickly some word from lang1 to lang2.

Commands
========

Command: @g lang1 lang2 data
Description: Translate the data from lang1 to lang2.
"""

from gdict import GoogleTranslator, shape
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg
from ameliabot.cmd import command

class Translator(object):
    def __init__(self, server):
        self.source = GoogleTranslator()
        xmap(server, 'CMSG', self.translate)

    @command('@g lang1 lang2 data')
    def translate(self, server, nick, user, host, target, msg, lang1, lang2, data):
        data = shape(self.source.translate(data, lang1, lang2))
        send_msg(server, target, data)
    
install = Translator







