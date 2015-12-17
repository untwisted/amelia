"""
"""

from untwisted.plugins.irc import send_msg
from untwisted.task import sched
from random import *
from re import split
from os.path import dirname, join

def install(server, chan_list, timeout=480):
    fd = open(join(dirname(__file__), 'quote_database'), 'r')
    data = fd.read()
    fd.close()
    list_quote = split('\n+', data)
    
    sched.after(timeout, send_quote, False,  
                server, chan_list, list_quote)

def send_quote(server, chan_list, list_quote):    
    for ind in chan_list:
        data = choice(list_quote)
        send_msg(server, ind, data)







