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
    count = 0
    def countArrangement(self, N: int) -> int:
        Solution.count = 0
        candidates = set(range(1, N+1))
        self.dfs(1, N, candidates)
        return Solution.count

    def dfs(self, cur, N, candidates):
        if cur > N:
            Solution.count += 1
            return
        for can in candidates:
            if can % cur == 0 or cur % can == 0:
                self.dfs(cur + 1, N, candidates - set([can, ]))

print(Solution().countArrangement(3))