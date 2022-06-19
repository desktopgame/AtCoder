# https://atcoder.jp/contests/abc255/tasks/abc255_d
# NOTE
# https://atcoder.jp/contests/abc255/editorial/4109
import sys
import bisect
from typing import List

nq: List[int] = list(map(int, sys.stdin.readline().split(' ')))
[N, Q] = nq
A = list(map(int, sys.stdin.readline().split(' ')))

A.sort()
# ループのたびにシグマを計算するとコストがかかるので累積和として持っておく
table: List[int] = [0]
for index, i in enumerate(A):
    table.append(table[index] + A[index])
for i in range(0, Q):
    x = int(sys.stdin.readline())
    K = bisect.bisect_left(A, x)
    # シグマ (X[i] - A[j]), (A[j] - X[i]) の計算
    w1 = K * x - table[K]
    w2 = -((N - K) * x) + table[N] - table[K]
    print(w1 + w2)