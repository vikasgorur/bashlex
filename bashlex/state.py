from bashlex import flags
from bashlex import utils

parserstate = lambda: utils.typedset(flags.parser)
