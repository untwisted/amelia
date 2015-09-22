from untwisted.network import xmap

def install(server):
    xmap(server, 'DCC SEND', dcc_get)

def dcc_get(*args):
    print 'args', args



