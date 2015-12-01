# -*- coding: utf-8 -*-
import pygame


class Wall(object):
    def __init__(self, position, direction, length):
        self._start_position = position
        self._direction = direction
        self._side_direction = direction.perp()
        self._end_position = position + direction * length
        self._length = length

    @property
    def start_position(self):
        return self._start_position

    @property
    def end_position(self):
        return self._end_position

    @property
    def direction(self):
        return self._direction

    @property
    def side_direction(self):
        return self._side_direction

    def render(self):
        from screen.Screen import Screen
        from utils.Color import BLACK
        pygame.draw.line(Screen().get_surface(), BLACK, self._start_position, self._end_position, 10)
