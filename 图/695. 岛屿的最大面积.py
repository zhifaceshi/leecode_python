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
    grid = None
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        Solution.grid = grid
        count = -1
        for i in range(m):
            for j in range(n):
                count = max(count, self.dfs(i, j, m, n))
        return count

    def dfs(self, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or Solution.grid[i][j] == 0:
            return 0
        Solution.grid[i][j] = 0
        return self.dfs(i+1, j, m, n) + \
               self.dfs(i-1, j, m, n) + \
               self.dfs(i, j+1, m, n) + \
               self.dfs(i, j-1, m, n) + 1


    