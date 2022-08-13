# https://atcoder.jp/contests/abc256/tasks/abc256_d
# NOTE
# *----*    (B)
#    *----* (A)
# ある区間Aがある区間Bの範囲内から開始する場合、それはある区間Bの終了をある区間Aの終了と同じにする
#    *----* (B)
# *----*    (A)
# ある区間Aがある区間Bの範囲内で終了する場合、それはある区間Aの終了をある区間Bの終了と同じにする
# *----* *----*
# 互いに独立して重なり合わない区間はマージできない
import sys
from typing import List

N: int = int(sys.stdin.readline())
LR: List[List[int]] = list(map(lambda i: list(map(int, sys.stdin.readline().split(' '))), range(0, N)))
LR.sort(key=lambda a: a[0])

def withInRange(a: List[int], b: List[int]) -> bool:
    return b[0] >= a[0] and b[0] <= a[1]

index: int = 0
while index < len(LR) - 1:
    s1 = LR[index]
    s2 = LR[index + 1]
    if withInRange(s1, s2):
        s1[1] = max(s1[1], s2[1])
        del LR[index + 1]
    else:
        index += 1

for s in LR:
    print(f'{s[0]} {s[1]}')