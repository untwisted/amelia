from untwisted.network import xmap
from untwisted.iostd import CONNECT

def load(con, plugin, *args, **kwargs):
    xmap(con, CONNECT, lambda con: plugin.install(
    con, *args, **kwargs))



