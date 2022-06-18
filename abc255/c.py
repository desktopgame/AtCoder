# https://atcoder.jp/contests/abc255/tasks/abc255_c
# NOTE
# ある数列 1, 2, 3 がある時、初項とは1のこと
# 3, 6, 9, 12 のような特定の間隔ごとに並んだ数列を等差数列と呼ぶ
# 公差とは、数列の数と数の間の差？
# 項数とは数列の長さのこと
import sys
import math
from typing import List

params: List[int] = list(map(int, sys.stdin.readline().split(' ')))
[X, A, D, N] = params

def solve(start: int, end: int, vv1, vv2) -> int:
    v1 = abs(A + (D * start) - X)
    v2 = abs(A + (D * end) - X)
    if v1 == vv1 and v2 == vv2:
        return min([v1, v2])
    if v1 < v2:
        return solve(start, start + math.ceil((end - start) / 2), v1, v2)
    else:
        return solve(start + math.ceil((end - start) / 2), end, v1, v2)

print(solve(0, N, N + 1, N + 1))