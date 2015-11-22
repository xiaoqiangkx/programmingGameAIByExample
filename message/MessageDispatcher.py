# -*- coding: utf-8 -*-
import time

import entity.EntityManager as EntityManager
from message.Message import Message
from utils.SortedSet import SortedSet

priorityQ = SortedSet(key=lambda x: x.getTime())


def discharge(receiver, message):
    receiver.handle_message(message)


def dispatch_message(delay, sender_id, receiver_id, msg, extra):
    receiver = EntityManager.get_entity_from_id(receiver_id)
    message = Message(sender_id, receiver_id, msg, extra)

    if delay <= 0.0:
        discharge(receiver, message)
    else:
        message.setTime(time.time() + delay)
        priorityQ.add(message)


def update():
    while len(priorityQ) > 0:
        current_time = time.time()
        message = priorityQ[0]

        if message.get_time() < current_time:
            receiver_id = message.get_received_id()
            receiver = EntityManager.get_entity_from_id(receiver_id)
            discharge(receiver, message)
            priorityQ.pop(0)
        time.sleep(2)


if __name__ == '__main__':
    import sys
    working_path = "%s\\%s".format(sys.path[0], "..")
    sys.path.insert(0, working_path)

    from entity.Miner import Miner
    miner1 = Miner()
    miner2 = Miner()
    dispatch_message(10, miner1.get_entity_id(), miner2.get_entity_id(), "hello 1-2", "")
    dispatch_message(0, miner2.get_entity_id(), miner1.get_entity_id(), "hello 2-1", "")

    update()

