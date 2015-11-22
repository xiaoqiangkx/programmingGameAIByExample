# -*- coding: utf-8 -*-
# ---------------------------负责注册管理所有的entity----------
# 1. 作为一个基础类，不关联具体的游戏功能类
# -----------------------------------------------------------
entity_map = {}


def register_entity(entity):
    entity_id = entity.get_entity_id()
    entity_map[entity_id] = entity


def un_register_entity(entity):
    entity_id = entity.get_entity_id()
    if entity_id in entity_map:
        entity_map[entity_id] = None


def get_entity_from_id(entity_id):
    return entity_map.get(entity_id, None)


if __name__ == '__main__':
    import sys
    sys.path.insert(0, "".join([sys.path[0], "\\.."]))
    from entity.Miner import Miner
    miner = Miner()
    miner_id = miner.get_entity_id()
    ret_miner = get_entity_from_id(miner_id)