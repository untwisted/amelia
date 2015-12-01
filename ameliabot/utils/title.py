import urllib2
import urllib
from re import compile, search, IGNORECASE,  DOTALL

STR_TITLE = '<title>(?P<data>.+?)</.+?>'
REG_TITLE = compile(STR_TITLE, IGNORECASE | DOTALL)

class Title(object):
    """ This class is used to obtain url titles. """
    def __init__(self):
        self.opener            = urllib2.build_opener()
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        self.MAX_SIZE          = 262144

    def get_title(self, url):
        data       = self.get_page(url)
        field      = search(REG_TITLE, data)
        page_title = field.group('data')

        return page_title

    def get_page(self, url):
        url = self.opener.open(url, timeout=0.5)
        data = url.read(self.MAX_SIZE)
        return data


