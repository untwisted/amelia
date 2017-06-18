"""
Overview
========

This plugin show an welcome message whenever an user joins a channel where the bot is in.

"""

from quickirc import send_msg
from untwisted.network import xmap

def install(server):
    xmap(server, 'JOIN', send_welcome)

def send_welcome(server, nick, user, host, channel):
        send_msg(server, channel, 'Welcome to our relaxed place !')










