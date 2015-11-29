# -*- coding: utf-8 -*-
import pygame

from pattern.Singleton import Singleton
from utils.Color import WHITE
from common.TIDs import TID_GAME_NAME


@Singleton
class Screen(object):
    def __init__(self):
        pygame.init()
        self.size = (500, 400)
        self.title = (TID_GAME_NAME)
        self.screen_surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        # draw on the surface object
        self.screen_surface.fill(WHITE)

    def get_surface(self):
        return self.screen_surface

    def refill(self):
        self.screen_surface.fill(WHITE)

    def get_size(self):
        return {'width': self.size[0], 'height': self.size[1]}