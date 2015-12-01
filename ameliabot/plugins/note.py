"""

"""

from untwisted.task import sched
from ameliabot.utils import codepad
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg

def install(server):
    xmap(server, ('CMSG', '.note_add'), note_add)
    xmap(server, ('CMSG', '.note_rm'), note_rm)

def note_add(server, (nick, user, 
                    host, target, msg, ), inc, to, *args):
    data = ' '.join(args) 
    sched.after(int(inc), remember, True, server, nick, to, data)

def note_rm(server, (nick, user, host, target, msg,), inc):
    sched.unmark(int(inc), remember)

def remember(server, nick, to, data):
    send_msg(server, to, '%s:%s' % (nick, data))






