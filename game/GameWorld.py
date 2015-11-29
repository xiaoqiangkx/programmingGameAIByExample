# -*- coding: utf-8 -*-

from pattern.Singleton import Singleton
from entity.Vehicle import Vehicle
from maths.Vector import Vector2
from logger.LogManager import LogManager
from utils.Color import BLUE


@Singleton
class GameWorld(object):
    def __init__(self):
        self.vehicle1 = Vehicle(self)
        self.vehicle2 = Vehicle(self)
        self.vehicle1.set_position(Vector2(100, 100))
        self.vehicle2.set_position(Vector2(150, 100))
        self.vehicle2.set_color(BLUE)
        self._logger = LogManager.get_logger("GameWorld")

        # self.vehicle1.steer_behavior.set_pursuit_on(self.vehicle2)
        # self.vehicle2.steer_behavior.set_evade_on(self.vehicle1)
        self.vehicle1.steer_behavior.set_wander_on()
        self.vehicle2.steer_behavior.set_wander_on()

    def render(self):
        self.vehicle1.render()
        self.vehicle2.render()

    def update(self, time_elapsed):
        self.vehicle1.update(time_elapsed)
        self.vehicle2.update(time_elapsed)
        self._logger.info("speed 1:%s", self.vehicle1.get_speed())
        self._logger.info("speed 2:%s", self.vehicle2.get_speed())

    @staticmethod
    def getInstance():
        return GameWorld()


if __name__ == '__main__':
    game_world1 = GameWorld()
    game_world1.a = 1
    game_world2 = GameWorld()
    print("game_world2:", game_world2.a)
