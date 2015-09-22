"""
Author: Iury O. G. Figueiredo.
Name: mean
Description: It gives a complete description for a word in english.
Usage:

<Tau>.m home
<yu>home; noun; place of residence; institution for people needing special care; one's native place or country; adjective; of one's home; adverb; to or at home; verb (used without object); to go home or toward a specified point; noun; minihome; min&middot;i&middot;home; at home; idiom; in one's own residence; in one's own town or country; prepared or willing to receive social visits; in a familiar situation; at ease; well-informed; proficient; 
<yu>make evident to; clarify or emphasize for; home and dry; idiom; having safely achieved one's goal; home free; idiom; assured of finishing, accomplishing, succeeding, etc.; certain to be successfully finished, accomplished, secured, etc.; write home about; idiom; to comment especially on; remark on;
"""
from untwisted.plugins.irc import send_msg
from ameliabot.utils.dictapi import DictApi
from untwisted.network import xmap

source = DictApi()

def install(server):
    xmap(server, ('PRIVCHAN', '.m'), translate)

def translate(server, (nick, user, host, target, 
                    msg,), *args):

    data = ' '.join(args)
    defn = source.lookup(data)
    send_msg(server, target, defn)




