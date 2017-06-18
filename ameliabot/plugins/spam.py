from time import asctime
from random import choice
from untwisted.network import xmap
from quickirc import send_msg

class Spam(object):
    def __init__(self, server, db=['Ameliabot rocks'], excpt=['#freenode']):
        """

        """

        self.pmed = list()
        xmap(server, 'CMSG', self.send_spam)

        # The list of chans whose users shouldnt be spammed.
        self.db    = db
        self.excpt = excpt
        
        
    def send_spam(self, server, nick, user, host, target, msg):
        if host in self.pmed or target.lower() in self.excpt: 
            return
    
        msg = choice(self.db)
        self.pmed.append(host)
        send_msg(server, nick, msg)
    
install = Spam

