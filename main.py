# -*- coding: utf-8 -*-
import sys

import pygame
from pygame.locals import QUIT

from game.GameWorld import GameWorld
from screen.Screen import Screen

import time

G_Screen = Screen.getInstance()
G_GameWorld = GameWorld.getInstance()


def init():
    pass


def main_loop():
    # run the game loop
    cnt = 0
    last_time = time.time()
    while True:
        time_elapsed = time.time() - last_time
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        G_GameWorld.update(time_elapsed)
        G_GameWorld.render()
        pygame.display.update()
        cnt += 1
        pygame.time.delay(30)


if __name__ == '__main__':
    init()
    main_loop()
