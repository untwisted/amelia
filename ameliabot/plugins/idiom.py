"""
Author: Iury O. G. Figueiredo.
Name: idiom
Description: This plugin is used to translate words from an idiom to another.
Usage:

<Tau>.g pt en casa
<yu>"noun" "house","home","household","building","roof","abode","premises","habitation","edifice","fireside","shebang","household franchise","inhabitation","pigsty"

Observation: It accepts three parameters lang_x, lang_y, phrase. 
You need to know the google language key. In this example pt stands for portuguese
and en stands for english.
"""

from uxirc.misc import *
from ameliabot.utils.google import GoogleTranslator, shape
from untwisted.network import xmap

source = GoogleTranslator()

def install(server):
    xmap(server, ('PRIVCHAN', '.g'), translate)

def translate(
                server, 
                (
                    nick, user, 
                    host, target, 
                    msg,
                ),
                lang_x, lang_y, 
                *args
             ):

    data = ' '.join(args)
    data = source.translate(data, lang_x, lang_y)
    data = shape(data)
    send_msg(server, target, data)


