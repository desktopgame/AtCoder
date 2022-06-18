import sys
from typing import List

nq: List[int] = list(map(int, sys.stdin.readline().split(' ')))
[N, Q] = nq
A = list(map(int, sys.stdin.readline().split(' ')))
X = list(map(int, [sys.stdin.readline() for i in range(0, Q)]))
for target in X:
    operations = 0
    for source in A:
        operations += abs(target - source)
    print(operations)