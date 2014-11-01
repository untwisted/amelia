"""

"""

from untwisted.network import core
from os.path import expanduser, join, exists, dirname
from os import mkdir
from shutil import copyfile
import sys

def init():
    dir = join(expanduser('~'), '.amelia')
    rc  = join(dir, 'ameliarc')
    
    if not exists(dir):
        mkdir(dir)
    
    copyfile(join(dirname(__file__), 'ameliarc'), rc)

def run():    
    dir = join(expanduser('~'), '.amelia')
    rc  = join(dir, 'ameliarc')

    if not exists(rc): 
        print 'You must call amelia --init.'; return
    ENV = dict()
    execfile(rc, ENV)
    core.gear.mainloop()
    




