# https://atcoder.jp/contests/abc255/tasks/abc255_d
# NOTE
# https://atcoder.jp/contests/abc255/editorial/4109
import sys
import math
from typing import List

nq: List[int] = list(map(int, sys.stdin.readline().split(' ')))
[N, Q] = nq
A = list(map(int, sys.stdin.readline().split(' ')))

# A[k] < X[i] < A[k+1]
# となるような K を見つける
# Xよりも大きい値がAの中に見つからなければ len(A) を返す
def bisect(x: int, start: int, end: int) -> int:
    if start >= len(A) or end >= len(A):
        return len(A)
    v1 = abs(A[start] - x)
    v2 = abs(A[end] - x)
    if (end - start) == 1:
        if A[start] < x and A[end] < x:
            return bisect(x, start + 1, end + 1)
        return (start if x < A[start] else end)
    if v1 < v2:
        return bisect(x, start, start + math.ceil((end - start) / 2))
    else:
        return bisect(x, start + math.ceil((end - start) / 2), end)

A.sort()
for i in range(0, Q):
    x = int(sys.stdin.readline())
    K = bisect(x, 0, N - 1)
    # シグマ (X[i] - A[j]), (A[j] - X[i]) の計算
    w1 = sum(map(lambda j: x - A[j], range(0, K)))
    w2 = sum(map(lambda j: A[j] - x, range(K, N)))
    print(w1 + w2)