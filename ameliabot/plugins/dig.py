"""
Author: Iury O. G. Figueiredo.
Name: dig
Description: This plugin is used to do quick searches on google.
Usage:

<Tau>.find ameliabot
<yu>http://www.facebook.com/people/Amelia-Bot/501424478
"""

from random import choice
from ameliabot.utils.research import Research
from uxirc.misc import *
from untwisted.network import xmap

base = Research()

def install(server):
    xmap(server, ('PRIVCHAN', '.find'), find)

def find(
            server, 
            (
                nick, user, 
                host, target, 
                msg,
            ),
            *args 
       ):

    data = ' '.join(args)
    space = base.quick_search(v='0.1', q=data, safe='high')
    url = choice(space)

    #sends to the target
    #the target would be the channel
    send_msg(server, target, url)



