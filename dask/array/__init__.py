from __future__ import absolute_import, division, print_function
from multipledispatch import halt_ordering, restart_ordering
import blaze

halt_ordering()
from .core import Array, stack, concatenate, tensordot, transpose
from .blaze import np  # need to go through import process here
from .into import into # Otherwise someone might import later
                       # without ordering halted
from . import random
from .wrap import ones, zeros, empty
restart_ordering()
