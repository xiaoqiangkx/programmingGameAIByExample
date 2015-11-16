# -*- coding: utf-8 -*-
import pygame

from screen.Screen import Screen


class Triangle(object):
    def __init__(self, params):
        self.color = params['color']
        self.pointList = params['pointList']
        self.width = 1

    def addToParent(self):
        # 坐标是从左上角作为(0,0)坐标
        pygame.draw.polygon(Screen.getInstance().getSurface(), self.color,
                            self.pointList, self.width)

    def update(self):
        pygame.draw.polygon(Screen.getInstance().getSurface(), self.color,
                            self.pointList, self.width)

    def render(self):
        pass
