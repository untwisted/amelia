from ehp import *
import urllib

class DictApi(object):
    def __init__(self):
        self.url = 'http://api-pub.dictionary.com/v001?%s'

    def lookup(self, word):
        header = {
                    'vid': 'm4eprmf12blt8tfx6srduqen43yenonas10knflqr7',
                    'q':word
                 }

        page = urllib.urlopen(self.url % urllib.urlencode(header))

        data = page.read()
        return self.parse(data)

    def parse(self, data):
        content = ''

        xml = Html()

        tree = xml.feed(data)

        for indi in tree.sail():
            if indi.name == 'display_form':
                for indj in indi.sail():
                        if indj.name == META:
                            content += '%s\n' % indj.data

            if indi.name == 'partofspeech':
                content += '%s\n' % indi.attr['pos']
                
                for indj in indi.sail():
                    if indj.name == 'def':
                        for indw in indj.sail():
                            if indw.name == META:
                                content += '%s\n' % indw.data

            if indi.name == 'derivatives':
                content += '%s\n' % indi.attr['pos']

                for indj in indi.sail():
                    if indj.name == META:
                        content += '%s\n' % indj.data
       
        
        content = content.replace('CDATA[', '')
        content = content.replace('\n', '; ')
        return content




