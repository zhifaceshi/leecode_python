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


class Solution:
    count = set()
    def countSubstrings(self, s: str) -> int:
        dp = self.huiwen(s)
        # for d in dp:
        #     print(d)
        count = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] == True:
                    count += 1
        return count

    def huiwen(self, s):
        dp = build_2d_matrix(len(s), len(s), False)
        for l in range(len(dp)):
            dp[l][l] = True
        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

        return dp

s = 'aaa'
# s = 'abc'
print(Solution().countSubstrings(s))
