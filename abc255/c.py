# https://atcoder.jp/contests/abc255/tasks/abc255_c
# NOTE
# ある数列 1, 2, 3 がある時、初項とは1のこと
# 3, 6, 9, 12 のような特定の間隔ごとに並んだ数列を等差数列と呼ぶ
# 公差とは、数列の数と数の間の差？
# 項数とは数列の長さのこと
import sys
from typing import List

params: List[int] = list(map(int, sys.stdin.readline().split(' ')))
[X, A, D, N] = params
U = [A + (D * i) for i in range(0, N)] # 初項に項数の長さ分公差を足す
print(min(map(lambda v: abs(X - v), U)))