from quickirc import send_msg
from ameliabot.cmd import regcmd
from liblax.parser import run
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

def post(data, title, name):
    """
    """

    URL               = 'http://mathb.in'
    opener            = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    head = {'code':'$%s$' % data,
    'title': title,'name': name,
    'submit':'Save and get new URL'}

    ptr = opener.open(URL, urllib.parse.urlencode(head))
    return ptr.geturl()

class Mathb(object):
    def __init__(self, server):
        server.add_map('CMSG', self.build)
    
    @regcmd('@mathb (?P<exp>.+)$')
    def build(self, server, nick, user, 
                    host, target, msg, exp):

        try:
            data = str(run(exp))
        except Exception as e:
            send_msg(server, target, str(e))
        else:
            send_msg(server, target, post(data, 
                'Math formulae', 'Ameliabot'))
      
install = Mathb

