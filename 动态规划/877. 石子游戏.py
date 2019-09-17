import itertools
import collections
import math
import re
import sys
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

# 参考 https://leetcode-cn.com/problems/stone-game/solution/jie-jue-bo-yi-wen-ti-de-dong-tai-gui-hua-tong-yong/
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = build_3dmatrix(n, n, 2)
        for i in range(len(piles)):
            dp[i][i][0] = piles[i]
        for l in range(2, n+1):
            for i in range(n - l + 1):
                j = n - l + 1
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                # 如果先手选择左边是最大的
                if left > right:
                    dp[i][j][0] = left
                    # 作为后手，此时最优肯定别别人占据主动了
                    # 那么只能选择后手了
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]

        return dp[0][-1][0] - dp[0][-1][1]


