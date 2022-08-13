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
#
# 元々はマージされるたびに片方を削除していたが、マージされる要素は常にリストの先頭側にあり削除のコストが高い。
# ので、連結リストを使おうと思ったがPythonの標準ライブラリに連結リストはない。
# そのためインデックスをずらすだけにした。
import sys
from typing import List

N: int = int(sys.stdin.readline())
LR: List[List[int]] = list(map(lambda i: list(map(int, sys.stdin.readline().split(' '))), range(0, N)))
LR.sort(key=lambda a: a[0])

def withInRange(a: List[int], b: List[int]) -> bool:
    return b[0] >= a[0] and b[0] <= a[1]

index: int = 0
offset: int = 0
while offset + index < len(LR) - 1:
    s1 = LR[offset + index]
    s2 = LR[offset + index + 1]
    if withInRange(s1, s2):
        # s1[1] = max(s1[1], s2[1])
        # del LR[index + 1]
        s2[0] = s1[0]
        s2[1] = max(s1[1], s2[1])
        offset += 1
    else:
        print(f'{LR[offset + index][0]} {LR[offset + index][1]}')
        index += 1

print(f'{LR[offset + index][0]} {LR[offset + index][1]}')