# -*- coding: utf-8 -*-

import utils.CommonUtil as CommonUtil
from ai.StateMachine import StateMachine


class BaseGameEntity(object):
    def __init__(self):
        self.entity_id = CommonUtil.genID()
        self.state_machine = StateMachine(self)

    def getID(self):
        return self.entity_id

    def update(self):
        pass

    def handleMessage(self, message):
        self.state_machine.handleMessage(message)
