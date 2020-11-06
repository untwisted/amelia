"""
Overview
========

Used to reconnect if the connection dies.


"""

from untwisted.event import CLOSE
from ameliabot.core import connect

def install(server):
    server.add_map(CLOSE, reconnect)

def reconnect(server, err):
    connect(server.servaddr, server.port, server.nick,
    server.user, server.nick_passwd, server.adm_passwd, server.chan_list, 
    server.plugmap)






