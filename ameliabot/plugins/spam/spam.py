from time import asctime
from random import choice
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg

FILE_NAME = './plugins/spam/database'

with open(FILE_NAME, 'r') as fd:
    db = fd.read()
    db = db.split('\n')
   
pmed = list()

# The list of chans whose users shouldnt be spammed.
chan_list = ['#bottt']

def install(server):
    xmap(server, 'CMSG', send_spam)

def send_spam(server, nick, user, host, 
                            target, msg):
    
    if host in pmed or target.lower() in chan_list: 
        return

    msg = choice(db)
    pmed.append(host)
    send_msg(server, nick, msg)



