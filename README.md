Amelia
======

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

**Note:**  Amelia demands python3 to work.

~~~
pip install -r requirements.txt
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

Then edit your **./amelia/ameliarc** file to setup
your networks and channels as well as plugins.

Amelia allows one to set up plugin scheme per network.
Your ameliarc file would look alike the below one:

~~~python
from ameliabot.core import connect
from ameliabot.plugins import load
##############################################################################
import sys

# You can place your plugins at ~/.amelia # To use them inside this file just do.
# import plugin_package_name or import plugin_name

from os.path import expanduser, join
sys.path.append(join(expanduser('~'), '.amelia'))
##############################################################################
# The plugin imports.

from ameliabot.plugins import join
# from ameliabot.plugins import spam
# from ameliabot.plugins import advisor

from ameliabot.plugins import logmsg
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
# from ameliabot.plugins import booklist
from ameliabot.plugins import dcc_send
from ameliabot.plugins import dcc_get
from ameliabot.plugins import translator
from ameliabot.plugins import polyglot
from ameliabot.plugins import lichess
from ameliabot.plugins import antispam
from ameliabot.plugins import latex
from ameliabot.plugins import mathb


##############################################################################
# Initialize a connection to the irc server

freenode = connect('irc.freenode.org', 6667, 
'amelia', 'fuinho fuinho fuinho :fuinho',       
'PRIVMSG nickserv :IDENTIFY nick_passwd',    
'fooobarr', ['#not-math', '##math-offtopic', '#vy'])

# Install plugins in the connection.
# load(freenode, join)
# load(freenode, spam, db=['alpha', 'beta'])
# load(freenode, advisor, questions='questions', suggestions='suggestions')

load(freenode, tell)
load(freenode, troll, 'aeiuh', 8, 15)
load(freenode, calc, '4WERXG-VAGETKREGX')
load(freenode, url_title)
load(freenode, codebox)
load(freenode, codenv, 'python3', '=py', '=end')
load(freenode, codenv , 'c', '=c', '=end')
load(freenode, codenv, 'c++', '=c++', '=end')
load(freenode, codenv, 'd', '=d', '=end')
load(freenode, codenv, 'lua', '=lua', '=end')
load(freenode, codenv, 'ocaml', '=ocaml', '=end')
load(freenode, codenv, 'php', '=php', '=end')
load(freenode, codenv, 'perl', '=perl', '=end')
load(freenode, codenv, 'ruby', '=ruby', '=end')
load(freenode, codenv, 'scheme', '=scheme', '=end')
load(freenode, codenv, 'tcl', '=tcl', '=end')
load(freenode, note)
load(freenode, pipe)
load(freenode, seen)
load(freenode, keep_alive)
load(freenode, ircadm)
load(freenode, help)
load(freenode, quote)
load(freenode, translator)
load(freenode, polyglot)
load(freenode, lichess)
load(freenode, antispam, n_lines=5, n_secs=5, 
cmd='kick {chan} {nick} :Amelia rocks!')
load(freenode, latex)
load(freenode, mathb)

# load(freenode, dcc_send, '/home/tau/Downloads')
# load(freenode, dcc_get, '/home/tau/Downloads')

##############################################################################
# Initialize another connection...

# virtualife = connect('irc.virtualife.com.br', 6667, 
# 'ameliabot',                                 
# 'untwistedbot euler euler :Ameliabot',       
# 'NickServ IDENTIFY nick_passwd',    
# 'bot_passwd', ['#brasil'])

# load(virtualife, quick_search)
# load(virtualife, tell)
# load(virtualife, troll, 'aeiuh', 8, 15)
# load(virtualife, calc, '4WERXG-VAGETKREGX')
# load(virtualife, url_title)
# load(virtualife, codebox)
~~~


Once you have set your plugins, channels and networks
just issue:

~~~
amelia --run
~~~

## Command Format

The command format scheme follows the following scheme.

~~~
@command arg1 arg2 ... arg_n 'argument with spaces' "argument with spaces"
~~~

## Command Help

The command below lists all loaded plugins for a given network.

~~~
@plugins
~~~

In order to get help for a given plugin then issue.

~~~
@doc plugin_name
~~~

## Credentials

Some plugins demand a given user to be authenticated.

The command to authenticate with amelia is as follow. Such a command has
to be issued as a private message.

~~~
@login password
~~~

Once the user is logged, amelia will keep the user's host in memory. Whenever an user
issues a command that demands authentication, amelia will check the user host.


