from utils.misc import *
from time import asctime
from random import choice
from untwisted.network import xmap

FILE_NAME = './plugins/spam/database'

with open(FILE_NAME, 'r') as fd:
    db = fd.read()
    db = db.split('\n')
   
pmed = list()

chan_list = ['#bottt']

def install(server):
    xmap(server, 'PRIVCHAN', send_spam)

def send_spam(
                server, 
                nick, user, 
                host, target, 
                msg,
              ):
    
    target = target.lower()

    if not host in pmed and target in chan_list: 
        msg = choice(db)
        pmed.append(host)
        send_msg(server, nick, msg)
    ###########
