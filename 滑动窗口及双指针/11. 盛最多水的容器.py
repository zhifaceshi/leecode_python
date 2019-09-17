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


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxvalue = -1
        while i < j:
            maxvalue = max(maxvalue, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxvalue

print(Solution().maxArea( [1,8,6,2,5,4,8,3,7]))