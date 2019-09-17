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


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(0, nums, [], ret)
        return ret

    def dfs(self, i, nums, state_lst, ret):
        if i >= len(nums):
            ret.append(list(state_lst))
            return
        self.dfs(i+1, nums, state_lst, ret)
        self.dfs(i+1, nums, state_lst + [nums[i], ], ret)


print(Solution().subsets([1, 2, 3]))