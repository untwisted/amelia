Introduction
============

Ameliabot is implemented on top of untwisted framework. It uses some of the untwisted tools in its plugin architecture. The fact of untwisted
being such a modular and objective event driven framework makes ameliabot core be so small. The plugin api is neat and powerful.
There is a variety of plugins that perform different tasks such as calculating integrals or executing python code on the fly.

The standard irc commands follow the following format although it is possible to implement irc commands that follow a different pattern.

@command arg1 arg2 ... arg_n 'argument with spaces' "argument with spaces"

or

@command arg1 arg2 ... arg_n argument with spaces with no '' 

The latter one uses regex for the command template.

User Plugins
============

Plugin Template
===============

Irc Events
==========

Event Handles
=============

A Simple Plugin
===============

Command Parser
==============

## Standard Command Format

Regex Command Parser
=====================

Irc Commands
============

Irc Messages
============


Plugin Help System Scheme
=========================





