import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')

import functools


class Solution:
    A = None
    K = None

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        Solution.A = A
        Solution.K = K
        return self.dfs(len(A) - 1)

    @functools.lru_cache(maxsize=None)
    def dfs(self, i):
        if i < 0:
            return 0
        # if i == 0:
        #     return Solution.A[i]
        maxvalue = -1e14
        for j in range(1, Solution.K + 1):
            if i - j <-1:
                break
            # maxvalue = max(self.dfs(i - j) + max(Solution.A[i - j + 1: i + 1] + [0, ]) * (j), maxvalue)
            maxvalue = max(self.dfs(i - j) + self.get_max(i-j+1, i) * (j), maxvalue)
        return maxvalue
    @functools.lru_cache(maxsize=None)
    def get_max(self, j, i):
        #包含j，i
        if i == j:
            return Solution.A[i]
        return max(
            Solution.A[j], self.get_max(j+1, i)
        )


A = [1,15,7,9,2,5,10]
K = 3
print(Solution().maxSumAfterPartitioning(A, K))
# print(Solution().test_getmax(A,2,5))