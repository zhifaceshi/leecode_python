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
    def maxSubArray(self, nums):
        pre = MININF
        maxvalue = MININF
        for s in nums:
            pre = max(pre + s, s)
            maxvalue = max(maxvalue, pre)
        return maxvalue

s = [-2,1,-3,4,-1,2,1,-5,4]

print(Solution().maxSubArray(s))
