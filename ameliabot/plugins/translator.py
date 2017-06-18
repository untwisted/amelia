"""
Overview
========

Used to translate quickly some word from lang1 to lang2.

Commands
========

Command: @g lang1 lang2 data
Description: Translate the data from lang1 to lang2.
"""

from libdict import GoogleTranslator
from untwisted.network import xmap
from quickirc import send_msg
from ameliabot.cmd import regcmd

class Translator(object):
    def __init__(self, server):
        self.google_translator = GoogleTranslator()
        xmap(server, 'CMSG', self.translate)

    @regcmd('@g (?P<lang1>.+?) (?P<lang2>.+?) (?P<data>.+)$')
    def translate(self, server, nick, user, host, target, msg, lang1, lang2, data):
        data = self.google_translator.translate(data, lang1, lang2)
        send_msg(server, target, data)
    
install = Translator











