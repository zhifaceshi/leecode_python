import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')

# 归纳跳格子的问题
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = 0
        while index < len(bits) - 1:
            index += bits[index] + 1
        return index == len(bits) - 1


bits = [1, 1, 1, 0]
print(Solution().isOneBitCharacter(bits))
