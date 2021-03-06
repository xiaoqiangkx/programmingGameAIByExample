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
        self.pursuer = None

        self.evade_on = False
        self.evader = None

        self.wander_on = False
        self.wander_jitter = 1
        self.wander_radius = 1
        self.wander_distance = 1

        self.obstacle_avoid_on = False
        self._obstacles = []

        self.wall_avoid_on = False
        self._walls = []

        self._logger = LogManager.get_logger("SteeringBehaviors")

    def set_pursuit_on(self, evader):
        self.pursuit_on = True
        self.evader = evader

    def set_wander_on(self):
        self.wander_on = True

    def set_evade_on(self, pursuer):
        self.evade_on = True
        self.pursuer = pursuer

    def set_obstacle_avoid_on(self, obstacles):
        self.obstacle_avoid_on = True
        self._obstacles = obstacles

    def set_wall_avoid_on(self, walls):
        self.wall_avoid_on = True
        self._walls = walls

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

    def obstacle_avoidance(self, obstacles):
        import utils.consts as CONST
        import math
        # 1. 获取最近的物体
        box_length = CONST.MIN_DELETE_BOX_LENGTH +\
            self.vehicle.get_max_speed() / self.vehicle.get_max_speed() * CONST.MIN_DELETE_BOX_LENGTH

        self.vehicle.game_world.tag_obstacles_with_view_range(self.vehicle, box_length)

        local_position_of_closest_obstacle = None
        dist_to_closest_ip = float("inf")
        closest_obstacle = None

        for obstacle in obstacles:
            if obstacle.tag is False:
                continue

            from maths.Matrix import PointToLocalPosition
            local_position = PointToLocalPosition(obstacle.position,
                                                  self.vehicle.get_head_direction(),
                                                  self.vehicle.get_side_direction(),
                                                  self.vehicle.get_position())

            if local_position.x >= 0:
                expand_radius = obstacle.bounding_radius + self.vehicle.bounding_radius / 2

                if abs(local_position.y) < expand_radius:   # 表示相交
                    cx = local_position.x
                    cy = local_position.y

                    square_part = math.sqrt(expand_radius * expand_radius - cy * cy)

                    ip = cx - square_part
                    if ip <= 0:
                        ip = cx + square_part

                    if ip < dist_to_closest_ip:
                        dist_to_closest_ip = ip
                        closest_obstacle = obstacle
                        local_position_of_closest_obstacle = local_position

        # 2. 计算侧向力和制动力
        steering_force = Vector2(0, 0)
        if local_position_of_closest_obstacle:
            # 侧向力反比于x的距离，方向由bounding_radius和local_obstacle.y控制，这个比较精巧
            multiplier = 1.0 + (box_length - local_position_of_closest_obstacle.x) / box_length
            steering_force_y = (closest_obstacle.bounding_radius - local_position_of_closest_obstacle.y) * multiplier

            # 正向力由距离控制, x越大，力越大;
            steering_force_x = 0.2 * (closest_obstacle.bounding_radius - local_position_of_closest_obstacle.x)
            steering_force = Vector2(steering_force_x, steering_force_y)

        from maths.Matrix import VectorToWorldSpace
        return VectorToWorldSpace(steering_force, self.vehicle.get_head_direction(), self.vehicle.get_side_direction())

    def create_feelers(self):
        feelers = []
        feelers.append(self.vehicle.position + self.vehicle.get_head_direction() * self.vehicle.bounding_radius * 1)
        feelers.append(self.vehicle.position + self.vehicle.get_side_direction() * self.vehicle.bounding_radius * 1)
        feelers.append(self.vehicle.position + self.vehicle.get_head_direction().reverse_perp() * self.vehicle.bounding_radius * 1)
        return feelers

    def wall_avoidance(self, walls):
        feelers = self.create_feelers()    # 胡须只是几个点而已

        closest_point = None
        closest_dist = float("inf")
        intersect_feeler = None
        closest_wall = None

        from maths.Line import LineIntersection2D
        for feeler in feelers:
            for wall in walls:
                intersect_point = LineIntersection2D(self.vehicle.position,
                                                     feeler,
                                                     wall.start_position,
                                                     wall.end_position)

                if intersect_point is not None:
                    distance = (intersect_point - self.vehicle.position).length()
                    if distance < closest_dist:
                        closest_dist = distance
                        intersect_feeler = feeler
                        closest_point = intersect_point
                        closest_wall = wall

        steering_force = Vector2(0, 0)
        if closest_point is not None:
            force_value = (closest_point - intersect_feeler).length()

            steering_force = closest_wall.side_direction * force_value

        self._logger.info("force value:%s", steering_force)
        return steering_force

    def calculate(self):
        result = Vector2(0, 0)
        if self.pursuit_on and self.evader:
            result += self.pursuit(self.evader)

        if self.evade_on and self.pursuer:
            result += self.evade(self.pursuer)

        if self.wander_on:
            result += self.wander()

        if self.obstacle_avoid_on:
            result += self.obstacle_avoidance(self._obstacles)

        if self.wall_avoid_on:
            result += self.wall_avoidance(self._walls)

        return result


