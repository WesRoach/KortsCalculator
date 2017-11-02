# coding = utf-8

# Singleton.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


class Singleton:
    __single = None

    def instance():
        return Singleton.__single
    instance = staticmethod(instance)

    def __init__(self):
        if Singleton.__single:
            raise TypeError("Singleton is already instantiated")
        Singleton.__single = self
