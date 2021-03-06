# -*- coding: utf-8 -*-

from entity.BaseGameEntity import BaseGameEntity
from maths.Vector import Vector2
from utils.metaclass import M


class MovingEntity(BaseGameEntity):
    __metaclass__ = M
    __slots__ = ['_velocity', '_head_direction', '_side_direction', '_mass', '_max_speed',
                 '_max_force', '_max_turn_rate']

    def __init__(self, position, radius):
        BaseGameEntity.__init__(self, position, radius)
        self.velocity = Vector2(0, 1)
        self.head_direction = Vector2(0, 1)    # 指向实体的朝向
        self.side_direction = self.head_direction.perp()  # 垂直朝向的向量
        self.mass = 10.0                  # 质量
        self.max_speed = 1.0              # 最大速度
        self.max_force = 0              # 最大力
        self.max_turn_rate = 0          # 弧度每秒

    def set_position(self, value):
        self._position = value

    def get_position(self):
        return self._position

    def get_speed(self):
        return self.velocity.length()


if __name__ == '__main__':
    import sys
    working_path = "{0}\\{1}".format(sys.path[0], "..")
    sys.path.insert(0, working_path)

    moving_entity = MovingEntity()
    moving_entity.set_velocity(Vector2(2, 2))

    print moving_entity.get_velocity()
