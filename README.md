ameliabot
=========

A flexible ircbot written on top of untwisted framework.

Features
========

- **Interface with WollframAlpha**

- **Run python, c, c++, D, haskell, lua, ocalml, PHP, perl, ruby, scheme, tcl code inline or multiline way**

- **Share files with friends on irc**

- **A translator plugin**

- **A real time translator plugin**

- **Quick searches on google**

- **Url tittle extraction**

- **Database with tons of philosophical quotes**

- **Pipe channel messages to other channels**

- **A note system to leave msgs to friends**

- **A last seen plugin**

- **A nifty help system**

- **A neat plugin API**


Install
=======

**Note:** 
Ameliabot demands python2.

~~~
pip install untwisted
pip install ehp
pip install libpad
pip install gsearch
pip install libdict
pip install wolframalpha
pip install ameliabot
~~~

Usage
=====

The command below should be issued after the installation.

~~~
amelia --init
~~~

It will create the following dir/files.

~~~
~/.amelia/
    ameliarc

~~~

The file named ameliarc is ameliabot setup file. It is needed to set up
some config options in that file before running ameliabot.

**~/.amelia/ameliarc**

~~~python
from ameliabot.core import connect
##############################################################################
import sys

# You can place your plugins at ~/.amelia # To use them inside this file just do.
# import plugin_package_name or import plugin_name

from os.path import expanduser, join
sys.path.append(join(expanduser('~'), '.amelia'))
##############################################################################
# The plugin imports.

# from ameliabot.plugins import join
# from ameliabot.plugins import spam
from ameliabot.plugins import logmsg
from ameliabot.plugins import quick_search
from ameliabot.plugins import tell
from ameliabot.plugins import troll
from ameliabot.plugins import calc
from ameliabot.plugins import url_title
from ameliabot.plugins import codebox
from ameliabot.plugins import codenv
from ameliabot.plugins import note
from ameliabot.plugins import pipe
from ameliabot.plugins import seen
from ameliabot.plugins import keep_alive
from ameliabot.plugins import ircadm
from ameliabot.plugins import help
from ameliabot.plugins.quote import quote
from ameliabot.plugins import booklist
from ameliabot.plugins import dcc_send
from ameliabot.plugins import dcc_get
from ameliabot.plugins import translator
from ameliabot.plugins import polyglot
from ameliabot.plugins import lichess


##############################################################################

# Define the set of plugins that will be available.
# You can define a different scheme for each server.

def PLUGIN_SCHEME(server):
    """
    These are all ameliabot built in plugins.
    You can have more than one scheme for irc networks.

    Just implement new PLUGIN_SCHEME functions then pass it as argument
    to connect function.
    """

    # join.install(server)
    # spam.install(server, db=['Ameliabot rocks', 'Use ameliabot'], excpt=['#freenode'])
    # logmsg.LogMsg(server, '/home/tau')

    quick_search.install(server)
    tell.install(server)
    troll.install(server, 'aehiou', 4, 16)
    calc.install(server, '4WERXG-VAGETKREGX')
    url_title.install(server)
    codebox.install(server)
    codenv.install(server, 'python', '#py', '#end')
    codenv.install(server, 'c', '@c', '@end')
    note.install(server)
    pipe.install(server)
    seen.install(server)
    keep_alive.install(server)
    ircadm.install(server)
    help.install(server)
    quote.install(server)
    translator.install(server)
    polyglot.install(server)
    lichess.install(server)

    # Used to share files, set the correct folder where the files would be in.
    # booklist.BookList(server, '/home/tau/ircshare')
    # dcc_send.install(server, '/home/tau/ircshare')
    # dcc_get.install(server, '/home/tau/ircshare')

##############################################################################
# The channel where the bot will stay when at freenode.
FREENODE_CHANNEL_SCHEME = ['#ameliabot', '#vy']

##############################################################################
# It tells the bot to connect to freenode then use the plugins
# that we have defined in PLUGIN_SCHEME handle.
# It will join the channels #ameliabot, #vy and ##calculus at irc.freenode.org
server = connect('irc.freenode.org', 6667, 
                 'ameliabot',                                 
                 'untwistedbot euler euler :Ameliabot',       
                 'PRIVMSG nickserv :IDENTIFY nick_passwd',    
                 'bot_passwd', FREENODE_CHANNEL_SCHEME, PLUGIN_SCHEME)

##############################################################################

# It is possible to have more than one connection per bot process. 
# For such just calls connect as many times as needed.
# VIRTUALIFE_CHANNEL_SCHEME = ['#oldcine']
##############################################################################

# server = connect('irc.virtualife.com.br', 6667, 
                 # 'ameliabot',                                 
                 # 'untwistedbot euler euler :Ameliabot',       
                 # 'NickServ IDENTIFY nick_passwd',    
                 # 'bot_passwd', VIRTUALIFE_CHANNEL_SCHEME, PLUGIN_SCHEME)








~~~

After setting up the irc network, irc channels, nick, nick password then it is possible 
to run the bot with the following command.

~~~
amelia --run
~~~

Video
=====

This video shows ameliabot features as well as explaining how to set up the bot config file.

https://www.youtube.com/watch?v=JpjOOPX0s6o

Getting Help
============

The following ircbot commands to obtain help work on private message system.

~~~
Commands
========

Command: @plugins
Description: Print a list of available plugins.

Command: @doc plugin
Description: Print the docs for the given plugin.

~~~

**Example**

~~~
<Tau>@plugins
<ameliabot> calc codebox codenv help ircadm ircshare join keep_alive logmsg note pipe polyglot quick_search quote seen spam tell translator troll url_title
<Tau>@doc seen
<ameliabot>Overview
<ameliabot>========
<ameliabot>Used to check last time a peer was seen online.
<ameliabot>Commands
<ameliabot>========
<ameliabot>Command: @seen peer
<ameliabot>Description: Show how long a nick has been inactive.
~~~

Documentation
=============

[MANUAL.md](MANUAL.md)


Support
=======

#### Freenode

**Network:** irc.freenode.org

**Channel:** #untwisted





