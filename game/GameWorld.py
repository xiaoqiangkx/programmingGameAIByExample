# -*- coding: utf-8 -*-

from pattern.Singleton import Singleton
from entity.Vehicle import Vehicle


class GameWorld(Singleton):
    def __init__(self):
        self.vehicle1 = Vehicle(self)
        self.vehicle2 = Vehicle(self)

    def render(self):
        self.vehicle1.render()
        self.vehicle2.render()

    def update(self, time_elapsed):
        self.vehicle1.update(time_elapsed)
        self.vehicle2.update(time_elapsed)

    @staticmethod
    def getInstance():
        return GameWorld()


if __name__ == '__main__':
    game_world1 = GameWorld()
    game_world1.a = 1
    game_world2 = GameWorld()
    print("game_world2:", game_world2.a)
