"""
Overview
========

Used to login with the bot in order to make the bot join, leave, channel
and perform other irc operations.

Commands
========

Command: @login password
Description: Login with the bot.

Command: @irccmd "irc command"
Description: Make the bot send the irc command

Example
=======

<\tau> @login bot_password
<\amelia> Logged!
<\tau> @irccmd "JOIN #vy"

"""

from ameliabot.adm import is_adm
from untwisted.network import xmap
from quickirc import send_cmd
from ameliabot.cmd import command

def install(server, *args):
    xmap(server, 'CMSG', irc_cmd)
    xmap(server, 'PMSG', irc_cmd)

@command('@irccmd data')
def irc_cmd(server, nick, user, host, target, msg, data):
    # is_adm(host) checks whether the user is authenticated
    # in order to send back to the server the irc command.
    if is_adm(host): send_cmd(server, data)








