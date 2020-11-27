""" 
Overview
========

Used to list files that are being shared.

Commands
========

Command: @dcc-list
Description: List all files that exist in a given folder that was shared.

"""

from quickirc import send_msg
from ameliabot.cmd import command
import os

class BookList(object):
    def __init__(self, server, folder):
        """
        """

        self.folder = folder
        server.add_map('CMSG', self.list_folder)
    
    @command('@dcc-list')
    def list_folder(self, server, nick, user, host, target, msg):
        """
        """
        content = '\n'.join(os.listdir(self.folder))
        send_msg(server, target, content)
        