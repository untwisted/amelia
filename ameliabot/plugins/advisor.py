from time import asctime
from random import choice, randint
from untwisted.network import xmap
from quickirc import send_msg
from untwisted.timer import Timer
import os
import re

class Advisor(object):
    def __init__(self, server, questions, suggestions, pmed_file='pmed', 
                                            blacklist_file='blacklist', timeout=60 * 3):

        self.questions      = self.load(questions)
        self.suggestions    = self.load(suggestions)
        self.timeout        = timeout
        self.pmed           = self.load(pmed_file)
        self.pmed_file      = pmed_file
        self.blacklist      = self.load(blacklist_file)
        self.blacklist_file = blacklist_file
        xmap(server, 'JOIN', self.send_question)
        xmap(server, 'PMSG', self.check_answer)

    def load(self, filename):
        with open(filename, 'a+') as fd:
            return re.split('\n+', fd.read().strip().lower())

    def check_answer(self, server, nick, user, host, target, msg):
        if (nick in self.pmed or host in self.pmed) and \
                           not (nick in self.blacklist or host in self.blacklist):
            Timer(randint(0, self.timeout), lambda : 
                             send_msg(server, nick, choice(self.suggestions)))
            self.register_user(self.blacklist, self.blacklist_file, nick, host)

    def send_question(self, server, nick, user, host, channel):
        if not (host.lower() in self.pmed or nick.lower() in self.pmed): 
            Timer(randint(0, self.timeout), lambda : 
                            send_msg(server, nick, choice(self.questions)))
            self.register_user(self.pmed, self.pmed_file, nick, host)

    def register_user(self, lst, filename, nick, host):
        lst.append(nick.lower())
        lst.append(host.lower())
        with open(filename, 'a+') as fd:
            fd.write('%s\n%s\n' % (nick, host))

install = Advisor








