# -*- coding: utf-8 -*-
import time

import entity.EntityManager as EntityManager
from message.Message import Message
from utils.SortedSet import SortedSet

priorityQ = SortedSet(key=lambda x: x.getTime())


def discharge(receiver, message):
    receiver.handleMessage(message)


def dispatchMessage(delay, sender_id, receiver_id, msg, extra):
    receiver = EntityManager.getEntityFromID(receiver_id)
    message = Message(sender_id, receiver_id, msg, extra)

    if delay <= 0.0:
        discharge(receiver, message)
    else:
        message.setTime(time.time() + delay)
        priorityQ.insert(message)


def update():
    current_time = time.time()
    while len(priorityQ) > 0:
        message = priorityQ[0]
        if message.getTime() < current_time:
            receiver_id = message.getReceiverId()
            receiver = EntityManager.getEntityFromID(receiver_id)
            discharge(receiver, message)
            priorityQ.pop(0)


if __name__ == '__main__':
    import sys
