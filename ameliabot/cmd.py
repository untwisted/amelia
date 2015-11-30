from re import split, match, compile

def tokenize(data):
    """
    """

    data = split(' +', data)
    return iter(data)

def build(seq, reg=''):
    """
    """

    reg = seq.next()
    for ind in seq:
        reg = fmt(reg, ind)
    return reg

def fmt(reg, chk):
    """
    """

    if chk.startswith('-'): 
        return '%s %s' % (reg, chk)
    else: 
        return '%s (?P<%s>.+)' % (reg, chk)

def command(template):
    regex = build(tokenize(template))
    def shell(func):
        def handle(*args):
            struct = match(regex, args[-1])
            if struct: func(*args, **struct.groupdict())
        return handle
    return shell









