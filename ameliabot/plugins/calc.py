"""
Author: Iury O. G. Figueiredo
Name: calc
Description: This plugin uses wolfram alpha to perform mathematical operations.
Usage: 
<Tau>.euler d(x^2)/dy
<yu>(d)/(dy)(x^2) = 0
"""

from ameliabot.utils.mathapi import MathApi
from uxirc.misc import *
from untwisted.network import xmap

source = MathApi('4WERXG-VAGETKREGX')

def install(server):
    xmap(server, ('PRIVCHAN', '.euler'), euler)

def euler(
            server, 
            (
                nick, user, 
                host, target, 
                msg,
            ),
            *args
       ):

    data = ' '.join(args)

    output = source.submit(data)

    send_msg(server, target, output)


