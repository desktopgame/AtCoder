# https://atcoder.jp/contests/abc255/tasks/abc255_e
# NOTE
# https://atcoder.jp/contests/abc255/editorial/4098
# 無数の組み合わせが存在するが、その中であらかじめ指定されたラッキーナンバーが多く含まれる組み合わせを選びたい。
# わからなかったので早い段階で解説を確認
# まず、Aはその全てにおいてA[i]+A[i+1]=S[i]が成り立たないといけない
# ので、AはSより一つ余分に長い配列になる
# A[0]さえ決まれば、それ以降の要素は A[i] = S[i - 1] - A[i - 1] となる。
# A[0]にどんな値を設定した時にそれ以降のA[i]により多くのラッキーナンバーが含まれるかを調べる。
# ところで、A[i] = S[i - 1] - A[i - 1] の式は
# 必ずA[0]の値が引き継がれる。
# A[1]: S[0] - A[0]
# A[2]: S[1] - (S[0] - A[0])
# A[3]: S[2] - (S[1] - (S[0] - A[0]))
# この性質を利用すると、あらかじめSの差分を別テーブルに持っておくことで式がシンプルになる
# B[0] = 0
# B[1] = S[0] - B[0]
# B[2] = S[1] - (S[0] - B[0])
# B[3] = S[2] - (S[1] - (S[0] - B[0]))
# こんな感じのBがあれば、
# A[i] = pow(-1, i+1) * Z + B[i] になる。
# B[0]は絶対に0なので、そこにZを足せばピッタリA[i]となる。
# ただし、計算が入れ子になっていて常に `-前回の結果` となっているので符号は交互に入れ替わる。
# A[i]がX[j]と一致する個数が多い組み合わせを選ぶ方法。
# A[i] = pow(-1, i+1) * Z + B[i] = X[j]
# となる個数を数えて、最も大きくなるZを選ぶ。
# これを変形すると Z = pow(-1, i+1) * (X[j] - A[i])
# 1. pow(-1, i+1) * Z + B[i] - X[j] = 0
# 2. pow(-1, i+1) * Z + B[i] - X[j] = 0
import sys
from typing import List

nm: List[int] = list(map(int, sys.stdin.readline().split(' ')))
[N, M] = nm
S: List[int] = list(map(int, sys.stdin.readline().split(' ')))
X: List[int] = list(map(int, sys.stdin.readline().split(' ')))

# B[0] = 0
# B[1] = S[0] - B[0]
# B[2] = S[1] - (S[0] - B[0])
# B[3] = S[2] - (S[1] - (S[0] - B[0]))
def makeB(src: List[int]) -> List[int]:
    ret: List[int] = []
    for i in range(0, len(src) + 1):
        if i == 0:
            ret.append(0)
        else:
            ret.append(src[i - 1] - ret[i - 1])
    return ret

B: List[int] = makeB(S)

# A[i] = pow(-1, i+1) * Z + B[i]
Z = S[0]
A: List[int] = [(pow(-1, i + 2) * Z) + diff for i, diff in enumerate(B)]
assert(len(A) == N)

countmap = {}
for i in range(0, N):
    for j in range(0, M):
        C = pow(-1, i + 2) * (X[j] - B[i])
        if C not in countmap:
            countmap[C] = 1
        else:
            countmap[C] += 1

lower = -1
key = 0
for k, v in countmap.items():
    if v > lower:
        lower = v
print(lower)