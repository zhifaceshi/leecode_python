import itertools
import collections
import math
import re
import sys
from typing import List

MAXINF = float('inf')
MININF = -float('inf')


def read_int_lst():
    return list(map(int, input().split()))


def build_3dmatrix(a, b, c, val=0):
    data = []
    for i in range(a):
        tt = []
        for j in range(b):
            t = []
            for k in range(c):
                t.append(val)
            tt.append(t)
        data.append(tt)
    return data


def build_2d_matrix(a, b, val=0):
    data = []
    for i in range(a):
        t = []
        for j in range(b):
            t.append(val)
        data.append(t)
    return data


class Solution:
    def numTilings(self, N: int) -> int:
        dp = build_2d_matrix(N+1, 2, 0)
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(2, N+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2 * dp[i-1][1]
            dp[i][1] = dp[i-2][0] + dp[i-1][1]
        return dp[N][0] % (10 ** 9 + 7)





print(Solution().numTilings(4))