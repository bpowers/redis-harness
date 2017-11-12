import collections

# Config = collections.namedtuple('Config', ['name', 'use_flags', 'ldflags'])

class Config:
    def __init__(self, name, use_flags, ldflags=None, skip=False, defrag=False):
        self.name = name
        self.use_flags = use_flags
        self.ldflags = ldflags
        self.skip = skip
        self.defrag = defrag

configs = [
    Config('libc',          'USE_JEMALLOC=no'),
    Config('jemalloc',      'USE_JEMALLOC=yes',         defrag=True),
    Config('tcmalloc',      'USE_TCMALLOC_MINIMAL=yes'),
    Config('mesh',          'USE_MESH=yes',             defrag=True),
    # Config('mesh-alwayson', 'USE_JEMALLOC=no',          '-lmesh', skip=True),
    Config('hoard',         'USE_JEMALLOC=no',          '-lhoard -L/usr/local/lib'),
]
