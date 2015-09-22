"""
Author: Iury O. G. Figueiredo.
Name: dccg
Description: It is used to receive files automatically into self.folder.
It is a kind of dcc server where people could store files.
Once one sends a file to the bot running this plugin it would automatically accept the file
and store it into self.folder variable path.
"""
from untwisted.plugins.irc import *
from os.path import isfile
from untwisted.network import xmap
from untwisted.utils.stdio import CLOSE, CONNECT_ERR
from untwisted.tools import long_to_ip

class Get(object):
    def __init__(self, server, folder):
        self.folder = folder
        xmap(server, 'DCC SEND', self.dcc_get)

    def dcc_get(self, server, (nick, user, host, 
                        target, msg), filename, address, port, size):
    
        path = '%s/%s' % (self.folder, filename)

        if isfile(path):      
            send_msg(server, nick, 'File already exists.')
        else:
            fd = open(path, 'wb')
            dccclient = DccClient(long_to_ip(int(address)), 
                                        int(port), fd, int(size)) 
    
            def is_done(spin, msg):
                send_msg(server, nick, msg)
                fd.close()
    
            xmap(dccclient, DONE, is_done, 'Done.')
            xmap(dccclient, CLOSE, lambda spin, err: is_done(spin, 'Failed.'))
            xmap(dccclient, CONNECT_ERR, lambda spin, err: is_done("It couldn't connect."))
    
    



