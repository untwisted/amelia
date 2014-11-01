from ehp import *
import urllib
import urllib2
from web import *

def post(data, lang, opt=False):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    lang_map = {
            'c':'C',
            'cpp':'C++',
            'd':'D',
            'haskell':'Haskell',
            'lua':'Lua',
            'ocaml':'OCaml',
            'php':'PHP',
            'perl':'Perl',
            'python':'Python',
            'ruby':'Ruby',
            'scheme':'Scheme',
            'tcl':'Tcl'
    }

    url = 'http://codepad.org'

    head = {
        'code':data,
        'lang':lang_map.get(lang, 'Plain Text'),
        'submit':'Submit'
    }

    head['run'] = opt

    pointer = opener.open(url, urllib.urlencode(head))

    #output = pointer.re()
    new_url = pointer.geturl()

    return (pointer, new_url)

def sandbox(code, lang):
    pointer, new_url = post(code, lang, opt=True)
    output = pointer.read()
    
    html = Html()

    tree = html.feed(output)
    
    output = ''
    for indi in tree.sail():
        if indi.name == 'div':
            if indi.attr['class']== 'code':
                for indj in indi.sail():
                    if indj.name == 'pre':
                        for inde in indj:
                            if inde.name == DATA:
                                if inde.data.strip().rstrip():
                                    output = output + inde.data
                            elif inde.name == CODE:
                                output = output + code(inde.data)
                            elif inde.name == AMP:
                                output = output + amp(inde.data)
    return new_url, output
