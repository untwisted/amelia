from quickirc import send_msg
from untwisted.timer import Sched, CancelCall
from re import escape

def consume(seq):
    try:
        seq.next()
    except StopIteration:
        raise CancelCall

def send_lines(server, target, msg, delay=0.7):
    def lazy():
        for ind in msg.splitlines():
            send_msg(server, target, ind)
            yield    
    Sched(delay, consume, lazy())





