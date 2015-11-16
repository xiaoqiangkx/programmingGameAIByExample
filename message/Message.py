# -*- coding: utf-8 -*-
import time


class Message(object):
    def __init__(self, sender_id, receiver_id, msg, extra):
        """extra保存了未来设计者希望传递的参数，这样就不用提前增加参数了"""
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.msg = msg
        self.dispatch_time = time.time()
        self.extra = extra

    def setTime(self, new_time):
        self.dispatch_time = new_time

    def getTime(self):
        return self.dispatch_time

    def getReceiverID(self):
        return self.receiver_id
