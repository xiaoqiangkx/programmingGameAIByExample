# -*- coding: utf-8 -*-

next_valid_id = 1


def genID():
    global next_valid_id
    ret_id = next_valid_id
    next_valid_id += 1
    return ret_id
