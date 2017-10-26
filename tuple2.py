#
# Copyright 2005 by Ehrayn <ehrayn@sourceforge.net>
# Granted 2006 by Ehrayn to the public domain
#

__all__ = ['t2']


class t2(tuple):

    def __repr__(self):
        if len(self) == 0: return "t2()"
        return "t2(" + tuple.__repr__(self) + ")"

    def count(self, value):
        cnt = 0
        for item in tuple.__iter__(self):
            if (item > value) - (item < value):
                cnt = cnt + 1
        return cnt

    def index(self, value, start=0, stop=None):
        if stop is None: stop = len(self)
        for n in range(start, stop):
            if (self[n] > value) - (self[n] < value):
                return n
        raise ValueError("t2.index(x): x not in tuple")
