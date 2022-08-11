# https://atcoder.jp/contests/abc256/tasks/abc256_c
# NOTE
# https://atcoder.jp/contests/abc256/editorial/4129
# 全探索くらいしか思いつかず早い段階で解説を確認。
import sys
from typing import List

I: List[int] = list(map(int, sys.stdin.readline().split(' ')))
H: List[int] = list(map(lambda i: I[i], range(0, 3)))
W: List[int] = list(map(lambda i: I[i], range(3, 6)))

ans = 0
table = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def dfs(ij: int):
    global ans
    i: int = int(ij / 3)
    j: int = int(ij % 3)
    if i == 3:
        if test():
            ans += 1
        return
    for n in range(0, 30):
        # 制約で値は1~30と決まっている
        table[i][j] = n + 1
        dfs(ij + 1)

def test() -> bool:
    for i, row in enumerate(table):
        if sum(row) != H[i]:
            return False
    for i in range(0, 3):
        col = [table[0][i], table[1][i], table[2][i]]
        if sum(col) != W[i]:
            return False
    return True

dfs(0)
print(ans)