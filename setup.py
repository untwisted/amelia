#! /usr/bin/env python

from distutils.core import setup

setup(name="vy",
      version="0.1",
      packages=["ameliabot", 
                "ameliabot.plugins",
                "ameliabot.utils",
                "ameliabot.plugins.ircshare",
                'ameliabot.plugins.spam',
                'ameliabot.plugins.quote'],
      scripts=['amelia'],
      package_data={'ameliabot': ['ameliarc', '/ameliabot/ameliarc'],
                    'ameliabot.plugins.quote':['quote_database', '/ameliabot/plugins/quote/quote_database']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br")

















