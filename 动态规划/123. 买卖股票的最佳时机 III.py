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
        n = len(prices)
        K = 2
        if n == 0:
            return 0
        dp = build_3dmatrix(K+1, n+1, 2)

        for k in range(0, K+1):
            for i in range(0,n+1):
                if k == 0:
                    dp[0][i][1] = -float('inf')
                    continue
                if i == 0:
                    dp[k][0][1] = -float('inf')
                    continue

                # 规定买入的时候，k += 1
                # 假设k = 2，表示第二次买入
                # 则 dp[k][i-1][1] + prices[i-1] 表示第k次买入，此时卖出，因此是正确的
                dp[k][i][0] = max(dp[k][i-1][0], dp[k][i-1][1] + prices[i-1])
                dp[k][i][1] = max(dp[k][i-1][1], dp[k-1][i-1][0] - prices[i-1])
        # for d in dp:
        #     print(d)
        return dp[-1][-1][0]


nums = [0,3,1,4] # 6
# nums = [1,2,3,4,5]

print(Solution().maxProfit(nums))

