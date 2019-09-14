import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = 0
        while l < len(seats) and seats[l] == 0:
            l += 1

        r = len(seats) - 1
        while r >= 0 and seats[r] == 0:
            r -= 1
        a = math.ceil(self.sliding_window(seats) // 2)

        a = max( a,
                l, len(seats) - r -1)
        return a


    def sliding_window(self, seats):
        r = 0
        l = 0
        count = 0
        while l < len(seats) and r < len(seats):

            while l < len(seats) and seats[l] == 1:
                l += 1
            r = l
            while r < len(seats) and seats[r] == 0:
                r += 1
            count = max(count, r - l)
            l = r
        return count


nums = [1,0,0,0]
print(Solution().maxDistToClosest(nums))