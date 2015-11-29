# -*- coding: utf-8 -*-
from maths.Vector import Vector2


def PointToWorldSpace(target_local, heading, side, local_position):
    trans_point = target_local

    trans_matrix = C2DMatrix()
    trans_matrix.rotate(heading, side)
    trans_matrix.translate(local_position.x, local_position.y)

    trans_point = trans_matrix.transform_vector_2d(trans_point)
    return trans_point


class C2DMatrix(object):
    def __init__(self):
        self.matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]

    def rotate(self, heading, side):
        temp_matrix = C2DMatrix()
        temp_matrix.matrix = [
            [heading.x, heading.y,  0],
            [side.x,    side.y,     0],
            [0,         0,          1],
        ]

        self.multiply(temp_matrix)

    def multiply(self, temp_matrix):
        target_matrix = C2DMatrix().matrix
        for row in xrange(3):
            for col in xrange(3):
                target_matrix[row][col] = self.matrix[row][0] * temp_matrix.matrix[0][col] +\
                                          self.matrix[row][1] * temp_matrix.matrix[1][col] +\
                                          self.matrix[row][2] * temp_matrix.matrix[2][col]
        self.matrix = target_matrix

    def translate(self, offset_x, offset_y):
        temp_matrix = C2DMatrix()
        temp_matrix.matrix = [
            [1,         0,         0],
            [0,         1,         0],
            [offset_x,  offset_y,  1],
        ]

        self.multiply(temp_matrix)

    def transform_vector_2d(self, trans_point):
        x = self.matrix[0][0] * trans_point.x + self.matrix[1][0] * trans_point.y + self.matrix[2][0]
        y = self.matrix[0][1] * trans_point.x + self.matrix[1][1] * trans_point.y + self.matrix[2][1]
        return Vector2(x, y)


if __name__ == '__main__':
    vec1 = Vector2(1, 0)
    vec2 = point_to_world_space(vec1, Vector2(1, 1), Vector2(-1, 1), Vector2(1, 0))
    print vec2