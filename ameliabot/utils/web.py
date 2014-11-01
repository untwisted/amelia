from htmlentitydefs import name2codepoint as htmldef

def amp(name):
    value = htmldef[name]
    return unichr(value).encode('utf8') 

def code(value):
    return unichr(int(value)).encode('utf8')


