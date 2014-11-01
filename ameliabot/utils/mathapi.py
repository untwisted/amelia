import urllib2
import urllib

from ehp import *

class MathApi(object):
    def __init__(self, appid):
        self.appid = appid
        self.base_url = 'http://api.wolframalpha.com/v2/query?'
        self.headers = {'User-Agent':None}

    def submit(self, query):
        code = {'input':query, 'appid':self.appid}
        url = urllib.urlencode(code)
        req = urllib2.Request(self.base_url, url, self.headers)
        xml = urllib2.urlopen(req).read()
        return self.parse(xml)

    def parse(self, xml):
        html = Html()

        tree = html.feed(xml)

        output = ''

        for indi in tree.sail():
            if indi.name == 'plaintext':
                for indj in indi.sail():
                    if indj.name == DATA:
                        output = output + indj.data
                break
        return output

                

