# -*- coding: utf-8 -*-


class M(type):
    def __new__(cls, name, bases, classdict):
        for attr in classdict.get('__slots__', ( )):
            if attr.startswith('_'):
                def getter(self, attr=attr):
                    return getattr(self, attr[1:])

                def setter(self, val=0, attr=attr):
                    return setattr(self, attr[1:], val)

                classdict['get' + attr] = getter
                classdict['set' + attr] = setter
        return type.__new__(cls, name, bases, classdict)