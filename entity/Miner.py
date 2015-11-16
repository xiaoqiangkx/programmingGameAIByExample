# -*- coding: utf-8 -*-
from entity.BaseGameEntity import BaseGameEntity


class Miner(BaseGameEntity):
    def __init__(self):
        BaseGameEntity.__init__(self)

    def changeState(self, new_state):
        self.state_machine.changeState(new_state)

    def update(self):
        pass
