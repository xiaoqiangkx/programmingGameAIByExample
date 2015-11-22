# -*- coding: utf-8 -*-
import logging


class StateMachine(object):
    def __init__(self, owner):
        self.owner = owner
        self.cur_state = None
        self.global_state = None
        self.previous_state = None

    def change_state(self, new_state):
        if new_state and self.cur_state:
            logging.error("state is not valid")
            return

        self.cur_state.exit(self)
        self.cur_state = new_state
        self.cur_state.enter(self)

    def update(self):
        if self.global_state:
            self.global_state.execute()

        if self.cur_state:
            self.cur_state.execute()

    def handle_message(self, message):
        print message.get_msg()
