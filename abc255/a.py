# https://atcoder.jp/contests/abc255/tasks/abc255_a
# 行列の成分を表示する
import sys
from typing import List

line1: str = sys.stdin.readline()
line2: str = sys.stdin.readline()
line3: str = sys.stdin.readline()

rc: List[int] = list(map(int, line1.split(' ')))
mat1: List[int] = list(map(int, line2.split(' ')))
mat2: List[int] = list(map(int, line3.split(' ')))

r = rc[0] - 1
c = rc[1] - 1
matrix = [
    mat1,
    mat2
]
print(matrix[r][c])