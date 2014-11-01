""" 
Author: Iury O. G. Figueiredo.
Name: math
Description: It is used to post equations on mathbin.
Usage:

<Tau>.eq \sum_{i=0}^{n} f(i)
<yu>1 http://mathbin.net/92754
"""

from ameliabot.utils.mathbin import Mathbin
from uxirc.misc import *
from untwisted.network import xmap

source = Mathbin()

def install(server):
    xmap(server, ('PRIVCHAN', '.eq'), paste_latex)

def paste_latex(
            server, 
            (
                nick, user, 
                host, target, 
                msg,
            ),
            title, *args 
       ):

    data = ' '.join(args)
    url = source.post(data, title)
    send_msg(server, target, url)



