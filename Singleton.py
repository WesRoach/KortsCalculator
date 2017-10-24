class Singleton:
    __single = None
    def instance():
        return Singleton.__single
    instance = staticmethod(instance)

    def __init__(self):
        if Singleton.__single:
            raise TypeError, "Singleton is already instantiated"
        Singleton.__single = self
