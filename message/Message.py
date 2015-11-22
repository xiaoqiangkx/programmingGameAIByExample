# -*- coding: utf-8 -*-
import time
from utils.metaclass import M


class Message(object):
    __metaclass__ = M
    __slots__ = ['_sender_id', '_receiver_id', '_msg', '_dispatch_time', '_extra']

    def __init__(self, sender_id, receiver_id, msg, extra):
        """extra保存了未来设计者希望传递的参数，这样就不用提前增加参数了"""
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.msg = msg
        self.dispatch_time = time.time()
        self.extra = extra
