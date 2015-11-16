# -*- coding: utf-8 -*-
import random

from pattern.Singleton import Singleton
from screen.Screen import Screen
from sprite.Triangle import Triangle
from utils.Color import GREEN


class GameWorld(Singleton):
    def __init__(self):
        param = {'color': GREEN,
                 'pointList': ((50, 50), (100, 50), (57, 75)),
                 'screen': Screen()}
        self.triangle = Triangle(param)
        self.triangle.addToParent(Screen())

    def render(self):
        pass

    def update(self):
        self.triangle.update()

    @staticmethod
    def getInstance():
        return GameWorld()


if __name__ == '__main__':
    game_world1 = GameWorld()
    game_world1.a = 1
    game_world2 = GameWorld()
    print("game_world2:", game_world2.a)
