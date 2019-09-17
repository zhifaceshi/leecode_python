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
    def maxProfit(self, prices: List[int]) -> int:
        dp = build_2d_matrix(len(prices)+1, 2)
        prices = [0, ] + prices
        # 不可能存在的状态
        dp[0][1] = MININF
        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] -prices[i])

        return dp[-1][0]

nums = [7,1,5,3,6,4]
print(Solution().maxProfit(nums))

