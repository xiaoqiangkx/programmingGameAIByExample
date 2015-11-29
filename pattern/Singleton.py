# -*- coding: utf-8 -*-


def Singleton(cls, *args, **kw):
    instances = {}
    def _Singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _Singleton


class Test(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    a = Singleton()
    a.test = 1
    b = Singleton()
    print(b.test)
