#
# Copyright 2005 by Ehrayn <ehrayn@sourceforge.net>
# Granted 2006 by Ehrayn to the public domain
#

import sys
import types

__all__ = ['d2']

class d2(dict):


    def __repr__(self):
        if len(self) == 0: return "d2()"
        return "d2(" + dict.__repr__(self) + ")"

    def clear(self):
        raise TypeError("invalid clear() - d2 object is read-only")

    def fromkeys(self, k, default=None):
        raise TypeError("invalid fromkeys() - d2 object is read-only")

    def setdefault(self, k, default=None):
        raise TypeError("invalid setdefault() - d2 object is read-only")

    def pop(self, k, default=None):
        raise TypeError("invalid pop() - d2 object is read-only")

    def popitem(self):
        raise TypeError("invalid popitem() - d2 object is read-only")

    def update(self, d):
        raise TypeError("invalid update() - d2 object is read-only")

    def __delitem__(self, k):
        raise TypeError("invalid item delete - d2 object is read-only")

    def __setitem__(self, k, value):
        raise TypeError("invalid item assignment - d2 object is read-only")

