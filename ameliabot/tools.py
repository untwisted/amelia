from untwisted.plugins.irc import send_msg
from untwisted.task import sched

def send_lines(server, target, msg, delay=0.7):
    def lazy():
        for ind in msg.splitlines():
            send_msg(server, target, ind)
            yield    
    iter = lazy()
    def consume():
        try:
            iter.next()
        except StopIteration:
            sched.unmark(delay, consume)
    sched.after(delay, consume, False)

