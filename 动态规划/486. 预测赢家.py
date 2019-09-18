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


# 博弈类有趣的游戏

class Solution:
    nums = None
    def PredictTheWinner(self, nums: List[int]) -> bool:
        Solution.nums = nums
        return self.dfs(0, len(nums) - 1, 0) >= self.dfs(0, len(nums) - 1, 1)
    @functools.lru_cache(None)
    def dfs(self, i, j, state):

        if i == j:
            if state == 0:
                return Solution.nums[i]
            else:
                return 0

        if state == 0:
            left  = self.dfs(i+1, j, 1) + Solution.nums[i]
            right = self.dfs(i, j-1, 1) + Solution.nums[j]
            if left > right:
                return left
            else:
                return right
        else:
            # 为什么是min？
            # 因为，对方肯定会选择收益最高的，给我们留下收益最低的。
            # 因此我们应该取小的那个值。
            return min(self.dfs(i+1, j, 0), self.dfs(i, j-1, 0))



a = [0, ]
print(Solution().PredictTheWinner(a))

