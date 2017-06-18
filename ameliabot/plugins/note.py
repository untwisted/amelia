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

from collections import namedtuple, defaultdict

from untwisted.network import xmap

from quickirc import send_msg
from ameliabot.cmd import command, regcmd

MAX_NOTES_PER_PEER = 2
MAX_NOTES = 10

# source = (nick, user, host)
Message = namedtuple('Message', ('source', 'message'))

class Note(object):
    def __init__(self, server):
        xmap(server, 'CMSG', self.note_add)
        xmap(server, 'CMSG', self.note_del)
        xmap(server, 'JOIN', self.send_note)
        self.base = defaultdict(list)

    @regcmd(r'@note-add\s+(?P<peer>\S+)\s+(?P<data>.*)')
    def note_add(self, server, nick, user, host, target, msg, peer, data):
        msgs = self.base[peer.lower()]
        user_msgs = [m for m in msgs if m.source[1:] == (user, host)
                     or user.startswith('~') and m.source[2] == host]
        if len(user_msgs) + 1 > MAX_NOTES_PER_PEER:
            send_msg(server, target,
                '%s: you may leave no more than %d notes for "%s".' % (
                nick, MAX_NOTES_PER_PEER, peer))
        elif len(msgs) + 1 > MAX_NOTES:
            send_msg(server, target,
                '%s: there are too many notes saved for "%s".' % (
                 nick, peer))
        else:
            msgs.append(Message(
                source=(nick,user,host), message=data))
            self.base[peer.lower()] = msgs
	    send_msg(server, target,
		'%s: note for "%s" saved.' % (nick, peer))

    @command('@note-del peer')
    def note_del(self, server, nick, user, host, target, msg, peer):
        peer = peer.lower()
	msgs = self.base.get(peer, [])
	orig_len = len(msgs)
	msgs = [m for m in msgs if m.source[1:] != (user, host)]
        if msgs: self.base[peer] = msgs
        elif peer in self.base: del self.base[peer]
	send_msg(server, target or nick, '%s: %d notes deleted.' % (
	    nick, orig_len - len(msgs)))

    def send_note(self, server, nick, user, host, channel):
        if nick.lower() not in self.base: return
        for msg in self.base[nick.lower()]:
            send_msg(server, channel, '%s: <%s> %s' % (
                nick, '%s!%s@%s' % msg.source, msg.message))
        del self.base[nick.lower()]

install = Note








