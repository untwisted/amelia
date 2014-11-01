import urllib
import json

class Research(object):
    def __init__(self):
        self.url = 'http://ajax.googleapis.com/ajax/services/search/web?%s'


    def search(self, **kwargs):
        addr = self.url % urllib.urlencode(kwargs)

        page = urllib.urlopen(addr)

        data = page.read()

        return json.loads(data)


    def quick_search(self, **kwargs):
        """ Filter links """
        result = self.search(**kwargs)

        space = [ind['url'] 
            for ind in result['responseData']['results']]

        return space



