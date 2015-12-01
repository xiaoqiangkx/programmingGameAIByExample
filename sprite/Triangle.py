# -*- coding: utf-8 -*-
import pygame

from maths.Vector import Vector2
from logger.LogManager import LogManager
from screen.Screen import Screen


class Triangle(object):
    def __init__(self, params):
        self.point_list = ()
        self._logger = LogManager.get_logger("Triangle")
        self._color = params['color']
        self._center_point = params['center_point']
        self._width = params['width']
        self._side = params['side']
        self._head_direction = params['head_direction']

    def update_place(self, params):
        self._center_point = params.get('center_point', self._center_point)
        self._head_direction = params.get('head_direction', self._head_direction)

    def update_point_list(self):
        point1 = self._head_direction * self._side * 1.732 / 3 + self._center_point

        point2_dir = Vector2(-0.5 * self._head_direction.x - 1.732 / 2 * self._head_direction.y,
                             1.732 / 2 * self._head_direction.x - 0.5 * self._head_direction.y).normalized()

        point2 = point2_dir * self._side * 1.732 / 3 + self._center_point

        point3_dir = Vector2(-0.5 * self._head_direction.x + 1.732 / 2 * self._head_direction.y,
                             -1.732 / 2 * self._head_direction.x - 0.5 * self._head_direction.y).normalized()
        point3 = point3_dir * self._side * 1.732 / 3 + self._center_point

        self.point_list = (point1.to_tuple(), point2.to_tuple(), point3.to_tuple())

    def update(self, time_elapsed):
        self.update_point_list()

    def is_valid(self):
        return type(self.point_list) == tuple and len(self.point_list) == 3

    def render(self):
        if not self.is_valid():
            return

        # self._logger.info("point_list:%s", self.point_list)
        pygame.draw.polygon(Screen().get_surface(), self._color,
                            self.point_list, self._width)
        # TODO 如果穿过屏幕，那么当所有点都穿过屏幕时从上面开始画。

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
