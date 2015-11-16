# -*- coding: utf-8 -*-


class Singleton(object):
    def __new__(type):
        if '_the_instance' not in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance


class Test(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    a = Singleton()
    a.test = 1
    b = Singleton()
    print(b.test)
