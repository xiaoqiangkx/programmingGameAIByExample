# -*- coding: utf-8 -*-

def WrapAround(pos, width, height):
    from math.Vector import Vector2
    return Vector2(pos.x % width, pos.y % height)