""" 

"""

import libpad
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg
from ameliabot.cmd import command
import os

class BookList(object):
    def __init__(self, server, folder):
        """
        """

        self.folder = folder
        xmap(server, 'CMSG', self.list_folder)
    
    @command('@ircshare-list')
    def list_folder(self, server, nick, user, host, target, msg):
        """
        """
        print 'testt'
        content = '\n'.join(os.listdir(self.folder))
    
        url, _ = libpad.sandbox(content, '') 
        send_msg(server, target, url)
        




