import urllib, urllib2
import re
"""
Lang codes
LANG = ['pt', 'en', 'fr', 'af', 'sq', 'de', 
        'ar', 'hy', 'az', 'eu', 'be', 'bg', 
        'ca', 'zh-CN', 'ko', 'ht', 'hr', 'da',
        'sk', 'sl', 'es', 'et', 'fi', 'gl', 'cy', 
        'ka', 'el', 'lw', 'hi', 'nl', 'hu', 'id', 
        'ga', 'is', 'it', 'ja', 'la', 'lv', 'lt', 
        'mk', 'ms', 'mt', 'no', 'fa', 'pl', 'ro', 
        'ru', 'sr', 'sw', 'sv', 'tl', 'th', 'cs', 
        'tr' ,'uk' ,'ur' ,'vi' ,'yi', 'auto']

This class is used to translate text using google translator.
The auto code is referring to the language detection feature.
"""

class GoogleTranslator(object):
    def __init__(self):
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]

        self.addr     = 'http://translate.google.com/translate_a/t?client=t&%s&sl=%s&tl=%s' 

        self.rgphrase = '\[([^\[\]]+?),"(?:.+?)","",""\]'
        self.rgword   = '\[([^\[\]]+?),\[([^\[\]]+?)\]\]' 

    def translate(self, data, lang1, lang2): 
        code = urllib.urlencode({"text":data})

        url = self.addr % (code, lang1, lang2)

        pointer = self.opener.open(url) 

        reply = pointer.read()

        unpacked = self.unpack(reply)

        return unpacked

    def unpack(self, data):
        output = re.findall(self.rgword, data)

        if output:
            return output

        output = re.findall(self.rgphrase, data)

        return output


def shape(data):
    data = map(lambda x: ' '.join(x) if isinstance(x, tuple) else x, data)
    data = ''.join(data)
    return data

