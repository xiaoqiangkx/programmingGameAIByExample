# -*- coding: utf-8 -*-

from entity.BaseGameEntity import BaseGameEntity
import pygame


class Obstacle(BaseGameEntity):

    def __init__(self, game_world, position, radius, tag=False, scale=(1.0, 1.0)):
        BaseGameEntity.__init__(self, position, radius, tag, scale)
        self.game_world = game_world

    def update(self, time_elapsed):
        pass

    def render(self):
        from screen.Screen import Screen
        from utils.Color import BLACK
        pygame.draw.circle(Screen().get_surface(), BLACK, self.position.to_tuple(), self.bounding_radius, 1)
