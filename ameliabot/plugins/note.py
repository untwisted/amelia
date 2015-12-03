"""

"""

from untwisted.network import xmap
from untwisted.plugins.irc import send_msg
from ameliabot.cmd import command

class Note(object):
    def __init__(self, server):
        xmap(server, 'CMSG', self.note_add)
        xmap(server, 'CMSG', self.note_rm)
        xmap(server, 'JOIN', self.tell)
        self.base = {}

    @command('@note-add peer data')
    def note_add(self, server, nick, user, host, target,
                                         msg, peer, data):
        self.base[peer.lower()] = data

    @command('@note-del id')
    def note_rm(self, server, nick, user, host, target, peer):
        del self.base[peer.lower()]

    def tell(self, server, nick, user, host, channel):
        try:
            data = self.base[nick.lower()]
        except KeyError:
            pass
        else:
            send_msg(server, channel, '%s %s' % (nick, data))

install = Note




