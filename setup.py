#! /usr/bin/env python2

from distutils.core import setup

setup(name="ameliabot",
      version="1.4.0",
      packages=["ameliabot", 
                "ameliabot.plugins",
                'ameliabot.plugins.quote'],
      scripts=['amelia'],
      package_data={'ameliabot': ['ameliarc', '/ameliabot/ameliarc'],
                    'ameliabot.plugins.quote':['quote_database', '/ameliabot/plugins/quote/quote_database']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br",
      url='https://github.com/iogf/ameliabot',
      download_url='https://github.com/iogf/ameliabot/releases',
      keywords=['irc', 'ircbot', 'untwisted', 'freenode', 'ameliabot', 'amelia'],
      classifiers=[],
      description="A nifty IRC Bot written on top of untwisted framework")



























