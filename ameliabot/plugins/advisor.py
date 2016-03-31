from time import asctime
from random import choice, randint
from untwisted.network import xmap
from untwisted.plugins.irc import send_msg
from untwisted.timer import Timer
import os
import re

class Advisor(object):
    def __init__(self, server, questions, 
                            suggestions, pmed_file='pmed', timeout=60 * 3):
        """

        """
        
        self.questions   = self.load(questions)
        self.suggestions = self.load(suggestions)
        self.timeout     = timeout
        self.pmed        = self.load(pmed_file)
        self.pmed_file   = pmed_file
        xmap(server, 'JOIN', self.send_question)
        xmap(server, 'PMSG', self.check_answer)

    def load(self, filename):
        fd = open(filename, 'a+')
        return re.split('\n+', fd.read().strip().lower())

    def check_answer(self, server, nick, user, host, target, msg):
        if nick in self.pmed or host in self.pmed:
            Timer(randint(0, self.timeout), lambda : 
                             send_msg(server, nick, choice(self.suggestions)))

    def send_question(self, server, nick, user, host, channel):
        if not (host.lower() in self.pmed or nick.lower() in self.pmed): 
            Timer(randint(0, self.timeout), lambda : 
                            send_msg(server, nick, choice(self.questions)))
            self.register_user(nick, host)

    def register_user(self, nick, host):
        nick = nick.lower()
        self.pmed.append(nick.lower())
        self.pmed.append(host.lower())
        with open(self.pmed_file, 'a+') as fd:
            fd.write('%s\n%s\n' % (nick, host))

install = Advisor






