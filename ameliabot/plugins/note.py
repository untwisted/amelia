"""
Author: Iury O. G. Figueiredo.
Name: note
Description: This plugin is used to store small chunks of text
that will be displayed later.
Usage:

<Tau>.note_add 3 #&math This is a interesting plugin. I might use it to leave msgs to people.
<yu>Tau:This is a interesting plugin. I might use it to leave msgs to people.
<Tau>.note_add 5 #&math 5 seconds later i am displayed.
<yu>Tau:5 seconds later i am displayed.
<Tau>.note_add 300 #&math it will not be displayed since i will remove this with .note_rm 300
<Tau>.note_rm 300

"""

from untwisted.task import sched
from ameliabot.utils import codepad
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg

def install(server):
    xmap(server, ('PRIVCHAN', '.note_add'), note_add)
    xmap(server, ('PRIVCHAN', '.note_rm'), note_rm)

def note_add(server, (nick, user, 
                    host, target, msg, ), inc, to, *args):
    data = ' '.join(args) 
    sched.after(int(inc), remember, True, server, nick, to, data)

def note_rm(server, (nick, user, host, target, msg,), inc):
    sched.unmark(int(inc), remember)

def remember(server, nick, to, data):
    send_msg(server, to, '%s:%s' % (nick, data))




