import shlex

def command(template):
    fields = shlex.split(template)
    def shell(func):
        def handle(*args):
            data = shlex.split(args[-1])
            if fields[0] == data[0]: 
                func(*args, **dict(zip(fields[1:], data[1:])))
        return handle
    return shell

