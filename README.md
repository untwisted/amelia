ameliabot
=========

A flexible ircbot written on top of untwisted framework.

Install
=======

pip install untwisted
pip install ehp
pip install libpad
pip install gsearch
pip install gdict
pip install ameliabot    

**Note:** 
Ameliabot demands python2.

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

Ameliabot API
=============

**HOWTO**

[HOWTO.md](HOWTO.md)


Irc Channel
===========

**Network:**
irc.freenode.org

**Channel:**
#vy

**Nick:**
Tau




