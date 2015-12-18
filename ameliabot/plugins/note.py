"""
Overview
========

Used to add a note to a peer when he joins the channel.

Commands
========

Command: @note-add peer data
Description: Add a msg to be shown when a nick joins a channel where the bot is in.

Command: @note-del peer
Description: Remove a note from a nick.
"""

from untwisted.network import xmap
from untwisted.plugins.irc import send_msg
from ameliabot.cmd import command

class Note(object):
    def __init__(self, server):
        xmap(server, 'CMSG', self.note_add)
        xmap(server, 'CMSG', self.note_rm)
        xmap(server, 'JOIN', self.send_note)
        self.base = {}

    @command('@note-add peer data')
    def note_add(self, server, nick, user, host, target, msg, peer, data):
        self.base[peer.lower()] = data

    @command('@note-del peer')
    def note_rm(self, server, nick, user, host, target, peer):
        del self.base[peer.lower()]

    def send_note(self, server, nick, user, host, channel):
        try:
            data = self.base[nick.lower()]
        except KeyError:
            pass
        else:
            send_msg(server, channel, '%s %s' % (nick, data))

install = Note







