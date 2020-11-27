"""
Overview
========

This plugin is used to receive files automatically through dcc.

Usage
=====

Once this plugin is installed and a directory was set in your ameliarc then whatever files
that are sent to the bot it will be saved in directory that was chosen.

"""

from quickirc import send_msg, DccClient
from os.path import isfile, join
from untwisted.event import CLOSE, CONNECT_ERR, DONE
from untwisted.iputils import long_to_ip

class Get(object):
    def __init__(self, server, folder):
        self.folder = folder
        server.add_map('DCC SEND', self.dcc_get)

    def dcc_get(self, server, xxx_todo_changeme, filename, address, port, size):
    
        (nick, user, host, 
                        target, msg) = xxx_todo_changeme
        path = join(self.folder, filename)

        if isfile(path):      
            send_msg(server, nick, 'File already exists.')
        else:
            fd = open(path, 'wb')
            dccclient = DccClient(long_to_ip(int(address)), 
                                        int(port), fd, int(size)) 
    
            def is_done(dcclient, msg):
                send_msg(server, nick, msg)
                fd.close()
    
            dccclient.add_map(DONE, is_done, 'Done.')
            dccclient.add_map(CLOSE, lambda dccclient, ssock, err: is_done(ssock, 'Failed.'))
            dccclient.add_map(CONNECT_ERR, lambda dccclient, ssock, err: is_done("It couldn't connect."))
    
    
install = Get








