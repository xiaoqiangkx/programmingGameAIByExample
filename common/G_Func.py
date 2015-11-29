# -*- coding: utf-8 -*-

def WrapAround(pos, width, height):
    from maths.Vector import Vector2
    return Vector2(pos.x % width, pos.y % height)


def getStringFromTID(tid_str, *args):
    return tid_str.format(*args)


def RandomClamped(st, ed):
    import random
    max_dis = ed - st
    return max_dis * random.random() + st, max_dis * random.random() + st
