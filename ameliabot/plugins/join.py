from untwisted.plugins.irc import send_msg
from untwisted.network import xmap

def install(server):
    xmap(server, 'JOIN', send_welcome)

def send_welcome(server, nick, user, host, channel):
        send_msg(server, channel, 'Welcome to our relaxed place !')








