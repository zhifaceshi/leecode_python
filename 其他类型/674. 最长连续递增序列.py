import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 1
        ans = 1
        for a, b in zip(nums[:-1], nums[1: ]):
            if a < b:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)
        return ans
a = [1, 3, 5, 7]
print(Solution().findLengthOfLCIS(a))