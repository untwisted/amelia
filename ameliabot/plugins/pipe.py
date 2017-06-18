"""
Overview
========

This plugin is used to pipe channels. Whenever one types in a channel it appears in other.

Commands
========

Command: @pipe-add chan_x chan_y
Description: Pipes all text from chan_x to chan_y.

Command: @pipe-del chan_x chan_y
Description: Remove the pipe from chan_x to chan_y.

"""

from untwisted.network import xmap
from quickirc import send_msg
from ameliabot.cmd import command

mapping = dict()

def install(server):
    xmap(server, 'CMSG', pipe_add)
    xmap(server, 'CMSG', pipe_rm)
    xmap(server, 'CMSG', pipe_chan)

@command('@pipe-add chan_x chan_y')
def pipe_add(server, nick, user, host, target, 
               msg, chan_x, chan_y):

    chan_x, chan_y = chan_x.upper(), chan_y.upper()
    if not mapping.has_key((server, chan_x)):
        mapping[(server, chan_x)] = list()
    mapping[(server, chan_x)].append(chan_y)

@command('@pipe-del chan_x chan_y')
def pipe_rm(server, nick, user, 
                    host, target, msg, chan_x, chan_y):
    chan_x, chan_y = chan_x.upper(), chan_y.upper()
    mapping[(server, chan_x)].remove(chan_y)

def pipe_chan(server, nick, user, host, target, msg,):
    chan_list = mapping.get((server, target.upper()))
    if not chan_list: return

    for ind in chan_list:
        send_msg(server, ind, '(%s)%s %s' % (target, nick, msg))













