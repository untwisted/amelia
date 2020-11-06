from untwisted.event import CONNECT

def load(con, plugin, *args, **kwargs):
    con.add_map(CONNECT, lambda con: plugin.install(
    con, *args, **kwargs))



