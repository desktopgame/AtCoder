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
    loop_exit = True
    for n in range(0, 30):
        # 制約で値は1~30と決まっている
        if i == 2:
            n = W[j] - table[0][j] - table[1][j]
        elif j == 2:
            n = H[i] - table[i][0] - table[i][1]
        else:
            n = n + 1
            loop_exit = False
        # 残り一つの値がマイナスだったら制約を満たしていないので次へ
        if n > 0:
            # table[i][j] が n の時の他のあらゆる要素の組み合わせを確認する
            table[i][j] = n
            dfs(ij + 1)
        else:
            break
        # 一意に決まった値なら他の値を試す必要はない
        if loop_exit:
            break

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