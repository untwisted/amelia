"""
Overview
========

This plugin retrieves the docstring for each one of the implemented plugins.

Commands
========

Command: @plugins
Description: Show all available plugins.

Command: @doc plugin
Description Show the help for the plugin.

"""

from ameliabot.tools import send_lines
from untwisted.network import xmap
from ameliabot.cmd import command
from pkgutil import iter_modules
import ameliabot.plugins
import os.path

class Help(object):
    def __init__(self, server):
        xmap(server, 'PMSG', self.plugins)
    
    @command('@plugins')
    def plugins(self, server, nick, user, host, target, msg):
        dir = os.path.dirname(ameliabot.plugins.__file__)
        data = ''
        for _, name, _ in iter_modules([dir]):
            data = '%s %s' % (data, name)
        send_msg(server, nick, data)

    @command('@doc plugin')
    def plugins(self, server, nick, user, host, target, msg, plugin):
        doc = ''
        code = 'import ameliabot.plugins.%s\ndoc = ameliabot.plugins.%s.__doc__' 
        exec(code % (plugin, plugin))
        send_lines(server, nick, doc)

install = Help



