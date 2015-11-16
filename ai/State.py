# -*- coding: utf-8 -*-


class State(object):
    """状态本身不保存entity的所有信息"""

    def __init__(self):
        pass

    def enter(self, entity):
        pass

    def execute(self, entity):
        pass

    def exit(self, entity):
        pass
