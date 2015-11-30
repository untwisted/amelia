"""
Author: Iury O. G. Figueiredo.
Name: quote
Description: It holds a database with quotes.
Usage:
<Tau>.inspire
<yu>And thou, vast ocean! on whose awful face
"""

from untwisted.task import sched
from untwisted.network import xmap
from random import *
from re import split
from os.path import dirname, join
from untwisted.plugins.irc import send_msg

def install(server):
    fd   = open(join(dirname(__file__), 'quote_database'), 'r')
    data = fd.read()

    fd.close()
    list_quote = split('\n+', data)
    
    xmap(server, ('CMSG', '.inspire'), send_quote, list_quote)

def send_quote(server, (nick, user, host, target, 
                                        msg), list_quote):    

    data = choice(list_quote)
    send_msg(server, target, data)






