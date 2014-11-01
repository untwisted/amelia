"""
Author: Iury O. G. Figueiredo.
Name: survive
Description: Used to reconnect to a network when it has lost a connection.
"""

from untwisted.network import xmap
from untwisted.utils.stdio import CLOSE
from ameliabot.core import connect

def install(server):
    xmap(server, CLOSE, reconnect)

def reconnect(server, err):
    connect(server.servaddr, 
            server.port,
            server.nick,
            server.user,
            server.nick_passwd,
            server.adm_passwd,
            server.chan_list,
            server.plugmap)


