"""
Author: Iury O. G. Figueiredo.
Name: doc
Description: This plugin prints a codepad url with README file contents.
Usage:

<Tau>.help
<yu>http://codepad.org/BWCAQH2v
"""

from uxirc.misc import *
from utils import codepad
from untwisted.network import xmap

PATH = 'readme'

def initialize():
    fd = open(PATH, 'r')
    data = fd.read()
    fd.close()

    global url
    _, url = codepad.post(data, '')

def install(server):
    xmap(server, ('PRIVCHAN', '.help'), readme)

def readme(
                server, 
                (
                    nick, 
                    user, 
                    host, 
                    target, 
                    msg,
                )
           ):


    send_msg(server, target, url)

##############
initialize()
