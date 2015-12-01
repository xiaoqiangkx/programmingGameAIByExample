# -*- coding: utf-8 -*-


def LineIntersection2D(A, B, C, D):
    r_top = (A.y-C.y)*(D.x-C.x)-(A.x-C.x)*(D.y-C.y)
    r_bot = (B.x-A.x)*(D.y-C.y)-(B.y-A.y)*(D.x-C.x)

    s_top = (A.y-C.y)*(B.x-A.x)-(A.x-C.x)*(B.y-A.y)
    s_bot = (B.x-A.x)*(D.y-C.y)-(B.y-A.y)*(D.x-C.x)

    if r_bot == 0 or s_bot == 0:
        return None

    r = float(r_top) / r_bot
    s = float(s_top) / s_bot

    if 1 > r > 0 and 1 > s > 0:
        point = A + (B - A) * r
        return point
    else:
        return None
