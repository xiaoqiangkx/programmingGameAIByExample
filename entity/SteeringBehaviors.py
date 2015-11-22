# -*- coding: utf-8 -*-
from maths.Vector import Vector2


class SteeringBehaviors(object):

    def __init__(self, vehicle):
        self.vehicle = vehicle

    def seek(self, target_position):
        target_velocity = (target_position - self.vehicle.get_position()).normalized() * self.get_max_speed()
        return target_velocity - self.vehicle.get_velocity()

    def calculate(self):
        return Vector2(0, 0)

