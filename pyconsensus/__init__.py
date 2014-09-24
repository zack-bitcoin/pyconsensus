from __future__ import division
import sys
try:
    import cdecimal
    sys.modules["decimal"] = cdecimal
except:
    pass

__title__      = "pyconsensus"
__version__    = "0.0.1"
__author__     = "Paul Sztorc and Jack Peterson"
__license__    = "GPL"
__maintainer__ = "Jack Peterson"
__email__      = "jack@dyffy.com"

from .pyconsensus import *
