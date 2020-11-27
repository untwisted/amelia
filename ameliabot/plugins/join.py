"""
Overview
========

This plugin show an welcome message whenever an user joins a channel where the bot is in.

"""

from quickirc import send_msg

def install(server):
    server.add_map('JOIN', send_welcome)

def send_welcome(server, nick, user, host, channel):
        send_msg(server, channel, 'Welcome to our relaxed place !')










