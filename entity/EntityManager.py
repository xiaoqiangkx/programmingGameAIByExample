# -*- coding: utf-8 -*-

entity_map = {}


def registerEntity(entity):
    entity_id = entity.getID()
    entity_map[entity_id] = entity


def unregisterEntity(entity):
    entity_id = entity.getID()
    if entity_id in entity_map:
        entity_map[entity_id] = None


def getEntityFromID(entity_id):
    return entity_map.get(entity_id, None)


if __name__ == '__main__':
    import sys
    sys.path.insert(0, "".join([sys.path[0], "\\.."]))
    print(sys.path)
    from entity.Miner import Miner
    miner = Miner()
    registerEntity(miner)
    ret_miner = getEntityFromID(miner.getID())
    print(ret_miner)
