# https://atcoder.jp/contests/abc255/tasks/abc255_b
# ある人間から最も近い距離のライトを全員分取得し、その最大値をとる
import math
import sys
from typing import List

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.x ^ self.y)

    def __eq__(self, __o: object) -> bool:
        if __o is Point:
            return self.x == __o.x and self.y == __o.y
        else:
            return False

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

def distance(a: Point, b: Point):
    xx = math.pow(b.x - a.x, 2)
    yy = math.pow(b.y - a.y, 2)
    return math.sqrt(xx + yy)

nk = list(map(int, sys.stdin.readline().split(' ')))
n = nk[0]
k = nk[1]
a = list(map(int, sys.stdin.readline().split(' ')))
assert(len(a) == k)

points: List[Point] = []
for i in range(0, n):
    xy = list(map(int, sys.stdin.readline().split(' ')))
    points.append(Point(xy[0], xy[1]))

lights: List[Point] = []
for v in a:
    lights.append(points[v-1])

light_max = -1
for point in points:
    other_lights = filter(lambda light: light != point, lights)
    min_light = min(map(lambda light: distance(point, light), other_lights))
    if min_light > light_max:
        light_max = min_light
print(light_max)