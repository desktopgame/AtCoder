import sys
from typing import List

nq: List[int] = list(map(int, sys.stdin.readline().split(' ')))
[N, Q] = nq
A = list(map(int, sys.stdin.readline().split(' ')))
for i in range(0, Q):
    target = int(sys.stdin.readline())
    operations = 0
    for source in A:
        operations += abs(target - source)
    print(operations)