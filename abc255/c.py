# https://atcoder.jp/contests/abc255/tasks/abc255_c
# NOTE
# ある数列 1, 2, 3 がある時、初項とは1のこと
# 3, 6, 9, 12 のような特定の間隔ごとに並んだ数列を等差数列と呼ぶ
# 公差とは、数列の数と数の間の差？
# 項数とは数列の長さのこと
# 数列を全部並べ替えると時間がかかりすぎるので二分探索
import sys
import math
from typing import List

params: List[int] = list(map(int, sys.stdin.readline().split(' ')))
[X, A, D, N] = params

def solve(start: int, end: int) -> int:
    s = abs(end - start)
    if 1 < s < 100:
        U = [A + (D * i) for i in range(start, end)]
        return min(map(lambda v: abs(v - X), U))
    elif s <= 1:
        U = [A + (D * start), A + (D * end)]
        return min(map(lambda v: abs(v - X), U))
    v1 = abs(A + (D * start) - X)
    v2 = abs(A + (D * end) - X)
    if v1 < v2:
        return solve(start, start + math.ceil((end - start) / 2))
    else:
        return solve(start + math.ceil((end - start) / 2), end)

print(solve(0, N))