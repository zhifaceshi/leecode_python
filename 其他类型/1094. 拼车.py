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
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        area = [0] * 1001
        for num, s, e in trips:
            for i in range(s, e):
                area[i] += num
        for n in area:
            if n > capacity:
                return False
        return True
t =  [[2,1,5],[3,3,7]]
c = 5
print(Solution().carPooling(t, c))


