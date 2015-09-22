from untwisted.plugins.irc import send_msg

def send_lines(server, target, msg):
    for ind in msg.splitlines():
        send_msg(server, target, ind)

