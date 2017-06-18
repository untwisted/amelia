""" 
Overview
========

Used to list files that are being shared.

Commands
========

Command: @dcc-list
Description: List all files that exist in a given folder that was shared.

"""

import libpad
from untwisted.network import xmap
from quickirc import send_msg
from ameliabot.cmd import command
import os

class BookList(object):
    def __init__(self, server, folder):
        """
        """

        self.folder = folder
        xmap(server, 'CMSG', self.list_folder)
    
    @command('@dcc-list')
    def list_folder(self, server, nick, user, host, target, msg):
        """
        """
        content = '\n'.join(os.listdir(self.folder))
    
        url, _ = libpad.sandbox(content, '') 
        send_msg(server, target, url)
        







