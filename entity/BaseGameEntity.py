# -*- coding: utf-8 -*-

import utils.CommonUtil as CommonUtil
from ai.StateMachine import StateMachine
from maths.Vector import Vector2


class BaseGameEntity(object):
    def __init__(self, position, radius, tag=False, scale=Vector2(1.0, 1.0)):
        import entity.EntityManager as EntityManager
        self.entity_id = CommonUtil.genID()
        EntityManager.register_entity(self)

        self.state_machine = StateMachine(self)

        self._position = position
        self._bounding_radius = radius
        self._tag = tag
        self.scale = scale

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def position(self):
        return self._position

    @property
    def bounding_radius(self):
        return self._bounding_radius

    def destroy(self):
        import entity.EntityManager as EntityManager
        EntityManager.un_register_entity(self)

    def get_entity_id(self):
        return self.entity_id

    def update(self):
        pass

    def handle_message(self, message):
        self.state_machine.handle_message(message)
