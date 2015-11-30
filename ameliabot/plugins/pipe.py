"""
Author: Iury O. G. Figueiredo.
Name: pipe
Description: This plugin is used to pipe a channel into other.
Usage:
I am actually on #&math and #&philosophy.

This is what happens over #&math
<yu>(#&philosophy)Tau hello
<yu>(#&philosophy)Tau is there somebody awaken
<Tau>.pipe_add #&math #&philosophy
>>> yu has mentioned your nick on #&philosophy <<<
<Tau>this is cool.
>>> yu has mentioned your nick on #&philosophy <<<

This is what happens over #&philosophy.
<yu>(#&math)Tau .pipe_add #&math #&philosophy
<yu>(#&math)Tau this is cool.

On #&math again.

<Tau>this is cool.
>>> yu has mentioned your nick on #&philosophy <<<
<Tau>sailorreality has spines on the ass. kkk
>>> yu has mentioned your nick on #&philosophy <<<
<Tau>.pipe_rm #&math #&philosophy
<Tau>hhe
<Tau>.pipe_rm #&philosophy #&math
<Tau>hehe
"""

from untwisted.network import xmap
from untwisted.plugins.irc import send_msg

mapping = dict()

def install(server):
    xmap(server, ('CMSG', '.pipe_add'), pipe_add)
    xmap(server, ('CMSG', '.pipe_rm'), pipe_rm)
    xmap(server, 'CMSG', pipe_chan)

def pipe_add(server, (nick, user, host, target, 
               msg, ), chan_x, chan_y):

    chan_x, chan_y = chan_x.upper(), chan_y.upper()
    if not mapping.has_key((server, chan_x)):
        mapping[(server, chan_x)] = list()
    mapping[(server, chan_x)].append(chan_y)

def pipe_rm(server, (nick, user, 
                    host, target, msg,), chan_x, chan_y):

    chan_x, chan_y = chan_x.upper(), chan_y.upper()
    mapping[(server, chan_x)].remove(chan_y)

def pipe_chan(server, nick, user, host, target, msg,):
    chan_list = mapping.get((server, target.upper()))
    if not chan_list: return

    for ind in chan_list:
        send_msg(server, ind, '(%s)%s %s' % (target, nick, msg))








