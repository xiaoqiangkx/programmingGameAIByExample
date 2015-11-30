# -*- coding: utf-8 -*-

from pattern.Singleton import Singleton
from entity.Vehicle import Vehicle
from maths.Vector import Vector2
from logger.LogManager import LogManager
from utils.Color import BLUE
from entity.Obstacle import Obstacle


class GameWorld(object):
    def __init__(self):
        self.obstacle1 = Obstacle(self, Vector2(300, 300), 30)
        self.obstacle2 = Obstacle(self, Vector2(500, 500), 40)
        self.obstacle3 = Obstacle(self, Vector2(600, 400), 20)
        self.obstacle_list = []
        self.obstacle_list.append(self.obstacle1)
        self.obstacle_list.append(self.obstacle2)
        self.obstacle_list.append(self.obstacle3)

        self.vehicle1 = Vehicle(self, Vector2(100, 100), 15)
        self.vehicle2 = Vehicle(self, Vector2(150, 100), 15)
        self.vehicle_list = []
        self.vehicle_list.append(self.vehicle1)
        self.vehicle_list.append(self.vehicle2)

        self.vehicle2.set_color(BLUE)
        self._logger = LogManager.get_logger("GameWorld")

        #self.vehicle1.steer_behavior.set_pursuit_on(self.vehicle2)
        #self.vehicle2.steer_behavior.set_evade_on(self.vehicle1)
        self.vehicle1.steer_behavior.set_wander_on()
        self.vehicle1.steer_behavior.set_obstacle_avoid_on(self.obstacle_list)
        self.vehicle2.steer_behavior.set_wander_on()
        self.vehicle2.steer_behavior.set_obstacle_avoid_on(self.obstacle_list)

    def tag_obstacles_with_view_range(self, vechicle, distance):
        for obstacle in self.obstacle_list:
            obstacle.tag = False

            local_distance = (vechicle.position - obstacle.position).length()
            if local_distance < distance:
                obstacle.tag = True

    def render(self):
        self.vehicle1.render()
        self.vehicle2.render()
        self.obstacle1.render()
        self.obstacle2.render()
        self.obstacle3.render()

    def update(self, time_elapsed):
        self.vehicle1.update(time_elapsed)
        self.vehicle2.update(time_elapsed)
        self.obstacle1.update(time_elapsed)
        self.obstacle2.update(time_elapsed)
        self.obstacle3.update(time_elapsed)
        # self._logger.info("speed 1:%s", self.vehicle1.get_speed())
        # self._logger.info("speed 2:%s", self.vehicle2.get_speed())


if __name__ == '__main__':
    game_world1 = GameWorld()
    game_world1.a = 1
    game_world2 = GameWorld()
    print("game_world2:", game_world2.a)
