# -*- coding: utf-8 -*-
import sys

import pygame
from pygame.locals import QUIT

from game.GameWorld import GameWorld
from screen.Screen import Screen

G_Screen = Screen.getInstance()
G_GameWorld = GameWorld.getInstance()


def init():
    pass


def mainLoop():
    # run the game loop
    cnt = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        G_GameWorld.update()
        G_GameWorld.render()
        pygame.display.update()
        cnt += 1
        pygame.time.delay(30)


if __name__ == '__main__':
    init()
    mainLoop()
