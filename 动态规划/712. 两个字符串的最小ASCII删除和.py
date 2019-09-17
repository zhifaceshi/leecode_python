import itertools
import collections
import math
import re
import sys
from typing import List
import functools

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

def convert(c):
    return ord(c)

# 编辑距离
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        dp = build_2d_matrix(len(s1) + 1, len(s2) + 1)
        s1 = [0, ] + [convert(c) for c in s1]
        s2 = [0, ] + [convert(c) for c in s2]
        count = 0
        for j in range(0,  len(s2)):
            count += s2[j]
            dp[0][j] = count
        count = 0
        for i in range(len(s1)):
            count += s1[i]
            dp[i][0] = count
        # print(s1)
        # print(s2)

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + s1[i],
                        dp[i][j - 1] + s2[j],
                        dp[i - 1][j - 1] + s1[i] + s2[j]
                    )
        return dp[-1][-1]

s1 = "sea"
s2 = "eat"
print(Solution().minimumDeleteSum(s1, s2))



