# -*- coding: utf-8 -*-
from maths.Vector import Vector2
from logger.LogManager import LogManager
from common.G_Func import RandomClamped
from maths.Matrix import PointToWorldSpace


class SteeringBehaviors(object):
    SLOW = 3
    NORMAL = 2
    FAST = 1

    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.pursuit_on = False
        self.evade_on = False
        self.wander_on = False
        self.wander_jitter = 1
        self.wander_radius = 1
        self.wander_distance = 1
        self.evader = None
        self.pursuer = None
        self._logger = LogManager.get_logger("SteeringBehaviors")

    def set_pursuit_on(self, evader):
        self.pursuit_on = True
        self.evader = evader

    def set_wander_on(self):
        self.wander_on = True

    def set_evade_on(self, pursuer):
        self.evade_on = True
        self.pursuer = pursuer

    def seek(self, target_position):
        target_velocity = (target_position - self.vehicle.get_position()).normalized() * self.vehicle.get_max_speed()
        return target_velocity - self.vehicle.get_velocity()

    def flee(self, target_position):
        distance = 100.0 * 100.0
        if distance > (target_position - self.vehicle.get_position()).normalized():
            return Vector2(0, 0)

        target_velocity = (target_position - self.vehicle.get_position()).normalized() * self.vehicle.get_max_speed()
        return self.vehicle.get_velocity() - target_velocity

    def arrive(self, target_position, deceleration):
        """speed由distance来进行控制"""
        distance = (target_position - self.vehicle.get_position()).length()

        if distance > 0:

            deceleration_weaker = 0.3

            speed = distance / (deceleration_weaker * deceleration)

            speed = min(speed, self.vehicle.get_max_speed())

            desired_velocity = target_position / distance * speed
            return desired_velocity - self.vehicle.get_velocity()

        return Vector2(0, 0)

    def pursuit(self, evader):
        # 判断智能体的朝向足够下，并且是同向
        relative_heading = Vector2.dot(evader.get_head_direction(), self.vehicle.get_head_direction())
        to_evade = evader.get_position() - self.vehicle.get_position()
        is_evade_forward = Vector2.dot(to_evade, self.vehicle.get_head_direction()) > 0

        if relative_heading < -0.95 and is_evade_forward:    # acos(0.95) = 18
            return self.arrive(evader.get_position(), SteeringBehaviors.NORMAL)

        look_ahead_time = to_evade.length() / (self.vehicle.get_max_speed() + evader.get_speed())
        return self.arrive(evader.get_position() + evader.get_velocity() * look_ahead_time, SteeringBehaviors.NORMAL)

    def evade(self, pursuer):
        relative_heading = Vector2.dot(pursuer.get_head_direction(), self.vehicle.get_head_direction())
        to_evade = pursuer.get_position() - self.vehicle.get_position()
        is_evade_forward = Vector2.dot(to_evade, self.vehicle.get_head_direction()) > 0

        if relative_heading < -0.95 and is_evade_forward:    # acos(0.95) = 18
            return self.flee(pursuer.get_position())

        look_ahead_time = to_evade.length() / (self.vehicle.get_max_speed() + pursuer.get_speed())
        return self.flee(pursuer.get_position() + pursuer.get_velocity() * look_ahead_time)

    def wander(self):
        wander_target = Vector2(*RandomClamped(-1, 1)) * self.wander_jitter
        wander_target = wander_target.normalized()
        wander_target *= self.wander_radius
        target_local = wander_target + Vector2(self.wander_distance, 0)

        target_world = PointToWorldSpace(target_local,
                                         self.vehicle.get_head_direction(),
                                         self.vehicle.get_side_direction(),
                                         self.vehicle.get_position())

        return target_world - self.vehicle.get_position()

    def calculate(self):
        result = Vector2(0, 0)
        if self.pursuit_on and self.evader:
            result += self.pursuit(self.evader)

        if self.evade_on and self.pursuer:
            result += self.evade(self.pursuer)

        if self.wander_on:
            result += self.wander()

        return result


