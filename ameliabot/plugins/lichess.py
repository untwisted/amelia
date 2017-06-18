"""
Overview
========

Used to show players' rating on lichess.org.

Commands
========

Command: @lichess player
Description: Shows the player's rating on lichess.org.

"""

import requests
from quickirc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import command

def getPlayerInfo(player):
    r = requests.get(('http://lichess.org/api/user/%s' % player))
    return r.json()

def ircOutput(playerinfo):
    if not playerinfo:
        return 'not found'
    return ("lichess.org - %s's performance: bullet: %s "
           "blitz: %s classical: %s" % 
           (playerinfo['username'], playerinfo['perfs']['bullet']['rating'],
            playerinfo['perfs']['blitz']['rating'], playerinfo['perfs']['classical']['rating']))

class Lichess:
	def __init__(self,server):
		xmap(server,'CMSG',self.getinfo)

	@command('@lichess player')
	def getinfo(self, server, nick, user, host, target, msg, player):
		result = getPlayerInfo(player)
		send_msg(server,target,str(ircOutput(result)))

install = Lichess

