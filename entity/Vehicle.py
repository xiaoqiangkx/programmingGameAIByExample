# -*- coding:utf-8 -*-

from entity.MovingEntity import MovingEntity
from common.G_Func import WrapAround
from sprite.Triangle import Triangle
from utils.Color import GREEN
from entity.SteeringBehaviors import SteeringBehaviors
from logger.LogManager import LogManager
from screen.Screen import Screen


class Vehicle(MovingEntity):
    def __init__(self, game_world):
        MovingEntity.__init__(self)
        self.game_world = game_world
        self._steer_behavior = SteeringBehaviors(self)

        data = self.get_vehicle_data()
        self.sprite = Triangle(data)

        self._logger = LogManager.get_logger("Vehicle")

    def set_color(self, color):
        self.sprite.color = color

    @property
    def steer_behavior(self):
        return self._steer_behavior

    def get_vehicle_data(self):
        param = {'color': GREEN,
                 'center_point': self.get_position(),
                 'head_direction': self.get_head_direction(),
                 'side': 20,
                 'width': 1
        }
        return param

    def render(self):
        self.sprite.render()

    def update_position(self):
        self.sprite.update_position({"center_point": self.position})

    def update(self, time_elapsed):
        steer_force = self._steer_behavior.calculate()
        acceleration = steer_force / self.mass

        self.velocity = acceleration * time_elapsed
        self.velocity = self.velocity.truncate(self.max_speed)

        self.position += self.velocity * time_elapsed

        if self.velocity.length() > 0.1:
            self.head_direction = self.velocity.normalized()
            self.side_direction = self.head_direction.perp()

        screen_size = Screen().get_size()
        self.position = WrapAround(self.position, screen_size['width'], screen_size['height'])

        self.update_position()
        self.sprite.update(time_elapsed)


