# -*- coding: utf-8 -*-
import pygame

from pattern.Singleton import Singleton
from utils.Color import WHITE


class Screen(Singleton):
    def __init__(self):
        pygame.init()
        self.size = (500, 400)
        self.title = ('AI Game')
        self.screen_surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        # draw on the surface object
        self.screen_surface.fill(WHITE)

    def getSurface(self):
        return self.screen_surface

    def getSize(self):
        return {'width': self.size[0], 'height': self.size[1]}

    @staticmethod
    def getInstance():
        return Screen()
