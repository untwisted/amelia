""" 
Author: Iury O. G. Figueiredo.
Name: booklist
Description: Used to list files that are insided dccs FOLDER path.
It lists on codepad.
Usage:

<Tau>.list_folder
<yu>http://codepad.org/XDvd9RMV
"""

from ameliabot.utils import codepad
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg

import os

class BookList(object):
    def __init__(self, server, folder):
        self.folder = folder
        xmap(server, ('PRIVCHAN', '.list_folder'), self.list_folder)

    def list_folder(self, 
                        server, 
                        (
                            nick, user, 
                            host, target, 
                            msg,
                        )
                    ):
    
        """ It lists the files into the FOLDER. """
        """ The user[3] contains the channel/nick of whom he spoke to. """
        content = '\n'.join(os.listdir(self.folder))
    
        """ See codepad.py file """
        addr, url = codepad.post(content, '') 
        send_msg(server, target, url)
        


