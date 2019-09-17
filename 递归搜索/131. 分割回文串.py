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

def check(s):
    return s == s[::-1]
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        self.dfs(s, [], ret)
        return ret
    def dfs(self,  s, state_lst, ret):
        if len(s) == 0:
            ret.append(list(state_lst))
        for i in range(1, len(s)+1):
            if check(s[:i]):
                state_lst.append(s[:i])
                self.dfs(s[i: ], state_lst, ret)
                state_lst.pop()

s = 'aab'
print(Solution().partition(s))