ameliabot
=========

A flexible ircbot written on top of untwisted framework.

Install
=======

This is a short script to run the latest version of ameliabot.

cd /tmp

git clone git://git.code.sf.net/p/untwisted/code untwisted-code
cd untwisted-code
python setupp.py install

git clone git://git.code.sf.net/p/uxirc/code uxirc-code
cd uxirc-code
python setup.py install

git clone https://github.com/iogf/ameliabot.git ameliabot-code
cd ameliabot-code
python setup.py install

That is all. 

Run ameliabot
=============

Once ameliabot is installed, you need to initialize ameliabot plugins
folder in your home directory.

Run the command below.

amelia --init

It will create.
~/.amelia/ameliarc

The ameliarc file is where you set up your plugin scheme,
network scheme and channels scheme. It means where you
want ameliabot to connect to.

    from ameliabot.core import connect
    
    import sys
    
    # You can place your plugins at 
    # ~/.amelia
    # To use them inside this file just do.
    # import plugin_package_name
    # or
    # import plugin_name
    from os.path import expanduser
    sys.path.append('%s/.amelia/' % expanduser('~'))
                   
    def PLUGIN_SCHEME(server):
        """
        These are all ameliabot built in plugins.
        You can have more than one scheme for irc networks.
    
        Just implement new PLUGIN_SCHEME functions then pass
        then to connect.
        """
    
        from ameliabot.plugins.ircshare import dccs
        dccs.Send(server, '~/ircshare')
    
        from ameliabot.plugins.ircshare import dccg
        dccg.Get(server, '~/ircshare')
    
        from ameliabot.plugins.ircshare import booklist
        booklist.BookList(server, '~/ircshare')
    
        from ameliabot.plugins import laugh
        laugh.install(server)
    
        from ameliabot.plugins import math
        math.install(server)
    
        from ameliabot.plugins import snarf
        snarf.install(server)
    
        from ameliabot.plugins import polyglot
        polyglot.install(server)
    
        from ameliabot.plugins import seen
        seen.Seen(server)
    
        from ameliabot.plugins import pipe
        pipe.install(server)
    
        from ameliabot.plugins import note
        note.install(server)
    
        from ameliabot.plugins import calc
        calc.install(server)
    
        from ameliabot.plugins.quote import quote
        quote.install(server)
    
        from ameliabot.plugins import survive
        survive.install(server)
    
        from ameliabot.plugins import logmsg
        logmsg.LogMsg(server, '/home/tau')
    
        from ameliabot.plugins import boxenv
        boxenv.BoxEnv(server, 'haskell', '@haskell', '', '@')
        boxenv.BoxEnv(server, 'python', '@python', '', '@')
        boxenv.BoxEnv(server, 'c', '@c', '', '@')
    
        from ameliabot.plugins import ircadm
        ircadm.install(server)
    
        from ameliabot.plugins.quote import auto_quote
        auto_quote.install(server, ['#vy'])
    
    
    # The channel where the bot will connect to.
    CHANNEL_SCHEME = ['#ameliabot', '#vy', '##calculus']
    
    # It tells the bot to connect to freenod then use the plugins
    # that we have defined in PLUGIN_SCHEME handle.
    # It will join the channels #ameliabot, #vy and ##calculus at irc.freenode.org
    server = connect('irc.freenode.org', 6667, 'ameliabot', 
                  'untwistedbot euler euler :Ameliabot', 'nick_passwd',
                  'bot_passwd', CHANNEL_SCHEME, PLUGIN_SCHEME)
    
    
    # The same way we did above. The interesting thing is we can have as many connections as we want.
    CHANNEL_SCHEME = ['#cine']
    
    # It will use the same plugin scheme but we could define a different handle for the plugins.
    server = connect('irc.virtualife.com.br', 6667, 'ameliabot', 
                  'untwistedbot euler euler :Ameliabot', 'nick_passwd',
                  'bot_passwd', CHANNEL_SCHEME, PLUGIN_SCHEME)
    



Now you can edit this file the way you need.

The standard plugins
====================
    # This plugin shows titles for links.
    from ameliabot.plugins import snarf

    Example:
    <Tau>https://github.com/iogf/ameliabot
    <ameliabot>iogf/ameliabot · GitHub
    
    This one permits sending stuff to wolfram alpha.    
    from ameliabot.plugins import calc

    # Example:
    <Tau>.euler integral sin(x^2) * x
    <ameliabot> integral sin(x^2) x dx = -1/2 cos(x^2)+constant

    # This one permits executing code at codepad.org.
    from ameliabot.plugins import boxenv

    # Example:
    <Tau>@python
    <Tau>def alpha():
    <Tau>   print 'this is cool.'
    <Tau>alpha()
    <Tau>@
    <ameliabot>this is cool.

    # This one can translate people phrases, it is a perfect translator for irc.
    from ameliabot.plugins import polyglot

    Example:
    <Tau>.polyglot_add en fr 189.84.245.210
    <Tau>this is cool.
    <ameliabot>Tau "ce est cool ."
    <Tau>.polyglot_rm en fr 189.84.245.210

    It can handle more than one at once.
    So you can add as many people ip as you want then it will translate
    every damn phrase whenever the people write.

    # This one can pipe channel A into channel B.
    from ameliabot.plugins import pipe

    # Example:
    <Tau>.pipe_add #philosophy #vy
    <Tau>.pipe_add #vy #philosophy
    
    It would pipe everything from philosophy to vy and vice versa.

    # This is a seen plugin.
    from ameliabot.plugins import seen

    # Example:
    <Tau>.seen soliloquy
    <ameliabot>soliloquy last seen 0:3:3 ago.
    
    # This one permits sharing stuff with people on irc.

    # THis one permits a dcc send, people can post stuff onto ircshare folder.
    from ameliabot.plugins.ircshare import dccg

    # This one offers a dcc get for people.
    from ameliabot.plugins.ircshare import dccs
    
    # THis one shows all the stuff at your ircshare folder.
    from ameliabot.plugins.ircshare import booklist

    # Just set a folder at your home dir named ircshare then it
    # will be shared with people on irc.

    # Example:
    .dcc_send alpha.py 4000

    It would tell the bot to send you a file named alpha.py that is stored at the bot's ircshare folder.

    # This one permits telling people things after a given interval of time.
    # It could remember you of things etc.
    from ameliabot.plugins import note

    <Tau>.note_add 3 #vy hafydd are you there
    <ameliabot>Tau ".note_add 3 hafydd de #vy vous êtes là"
    <ameliabot>Tau:hafydd are you there

    # This one has a nice database of insightful quotes.
    from ameliabot.plugins.quote import auto_quote

    # This one reconnects when the bot connection ends.
    from ameliabot.plugins import survive


The bot api
===========

You obviously will want to implement your own plugins.
The ameliabot api is untwisted based it turns everything easier to do.

A simple example of plugin would be.

    # say.py
    from uxirc.misc import *
    from untwisted.network import xmap
    
    def install(server):
        xmap(server, 'PRIVCHAN', say)
    
    def say(server, nick, user, host, target, msg):
            send_msg(server, target, 'You said: %s' % msg)
    


    # It would output.

    # <Tau>say hello
    # <ameliabot>You said: say hello
    
The xmap function is used to map the irc event to a handle.
In this case, the event is 'PRIVMSG' which is a string.

Whenevr a PRIVMSG irc event happens the handle say will be called with
the arguments corresponding to the event.  The uxirc that is a protocol implementation on top
of untwisted for irc parses the irc msgs coming from the server then generates the events.

So, you just need to bind an irc command from the server to a handle with xmap
then you will have your handles called whenever them happen.

Another example is.

    # join.py
    from uxirc.misc import *
    from untwisted.network import xmap
    
    def install(server):
        xmap(server, 'JOIN', send_welcome)
    
    def send_welcome(server, nick, user, host, channel):
            send_msg(server, channel, 'Welcome to our relaxed place !')
    



This one uses the 'JOIN' event. Whenever someone joins the channel
the handle send_welcome is called.


You can make as many bindings as you want to all kind of events.

For a complete list of irc events.
https://tools.ietf.org/html/rfc1459

Another good approach is just running amelia over a channel from a shell
then you can look at what amelia outputs, it will appear every event name.

Like in.

:morgan.freenode.net 372 ameliabot :- We would like to thank Private Internet Access
:morgan.freenode.net 372 ameliabot :- (https://www.privateinternetaccess.com/) and the other
:morgan.freenode.net 372 ameliabot :- organisations that help keep freenode and our other projects
:morgan.freenode.net 372 ameliabot :- running for their sustained support.
:morgan.freenode.net 372 ameliabot :-  
:morgan.freenode.net 372 ameliabot :- In particular we would like to thank the sponsor
:morgan.freenode.net 372 ameliabot :- of this server, details of which can be found above.
:morgan.freenode.net 372 ameliabot :-  
:morgan.freenode.net 376 ameliabot :End of /MOTD command.
:ameliabot MODE ameliabot :+i
:morgan.freenode.net 302 ameliabot :ameliabot=+~untwisted@189.84.245.210 
:ameliabot!~untwisted@189.84.245.210 JOIN #ameliabot
:morgan.freenode.net MODE #ameliabot +ns
:morgan.freenode.net 353 ameliabot @ #ameliabot :@ameliabot

These would be named, '372', '302', 'MODE', '353', ...
So if you want a handle to be called on '372' just map it with xmap.

I hope you enjoy amelia as i enjoyed.


Old repository
==============
http://ameliabot.sourceforge.net/



