import urllib2
import urllib

class Mathbin(object):
    def __init__(self):
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]


    def post(self, data, title='', shape='eq'):
        """ 
            Post data to mathbin.
            shape = 'eq'
            title = 'example'
            data = 'x^2'
        """

        code = urllib.urlencode({shape:data, 'title':title})

        url = 'http://www.mathbin.net/backend.html?%s' % code

        pointer = self.opener.open(url)

        output = pointer.read()
        
        return output.replace('\n', ' ')

