import sys
from typing import List

N: int = int(sys.stdin.readline())
A: List[int] = list(map(int, sys.stdin.readline().split(' ')))
P: int = 0
table: List[int] = list([0 for _ in range(0, 4)])

for i in range(0, N):
    Ai: int = A[i]
    table[0] += 1
    for j in reversed(range(0, len(table))):
        t: int = table[j]
        next: int = j + Ai
        table[j] = 0
        if next < len(table):
            table[next] += t
        else:
            P += t
print(P)