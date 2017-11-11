import collections

Config = collections.namedtuple('Config', ['name', 'use_flags', 'ldflags'])

configs = [
    Config('libc',          'USE_JEMALLOC=no',          ''),
    Config('jemalloc',      'USE_JEMALLOC=yes',         ''),
    Config('tcmalloc',      'USE_TCMALLOC_MINIMAL=yes', ''),
    Config('mesh',          'USE_MESH=yes',             ''),
    Config('mesh-alwayson', 'USE_JEMALLOC=no',          '-lmesh'),
    Config('hoard',         'USE_JEMALLOC=no',          '-lhoard -L/usr/local/lib'),
]
