# -*- coding: utf-8 -*-

import utils.CommonUtil as CommonUtil
from ai.StateMachine import StateMachine


class BaseGameEntity(object):
    def __init__(self):
        import entity.EntityManager as EntityManager
        self.entity_id = CommonUtil.genID()
        self.state_machine = StateMachine(self)
        EntityManager.register_entity(self)

    def destroy(self):
        import entity.EntityManager as EntityManager
        EntityManager.un_register_entity(self)

    def get_entity_id(self):
        return self.entity_id

    def update(self):
        pass

    def handle_message(self, message):
        self.state_machine.handle_message(message)
