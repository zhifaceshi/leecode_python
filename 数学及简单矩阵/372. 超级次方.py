import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')

# 肯定不行的算法，只能
# 4 / 54 个通过测试用例
# (a*b)%c = ((a%c)*(b%c)%c
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        pre = 1
        c = 1337
        for base in b:
            pre = ((pre ** 10) % c) * ((a ** base) % c) % c
        return pre

print(Solution().superPow(2, [1, 0]))