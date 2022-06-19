# https://atcoder.jp/contests/abc255/tasks/abc255_d
# NOTE
# https://atcoder.jp/contests/abc255/editorial/4109
# 最初は単純に二重ループで差分の和を取っていたが、これだとTLE。
# 解説を見ると、
# Aの数列をxより小さいものと大きいもので分割し、
# 大きい方なら：A[i]-x
# 小さい方なら：x-A[i]
# のように差分の和をとっている。
# 輪をとるとき、ループごとに毎回計算するのではなく
# 予めテーブルに値をメモしておく。
# (三角関数をテーブル化して高速化するのに近い方法？)
# 特に和を高速に参照するためのテーブルを累積和、というらしい。
# これをループ前に計算しておくとループ内ではテーブルの値を参照するだけですむ。
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
    # A[k] < X[i] < A[k+1] となるような K を見つける
    K = bisect.bisect_left(A, x)
    # シグマ (X[i] - A[j]), (A[j] - X[i]) の計算
    w1 = K * x - table[K]
    w2 = -((N - K) * x) + table[N] - table[K]
    print(w1 + w2)