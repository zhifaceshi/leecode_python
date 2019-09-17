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
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        ans = 0
        for s in S:
            if s == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                ans += 1
                count = 0
        return ans + count

s = "()))(("
print(Solution().minAddToMakeValid(s))
