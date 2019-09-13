import itertools
import collections
import math
import re
import sys
from typing import List

MAXINF = float('inf')
MININF = -float('inf')

def show_grid(grid):
    for d in grid:
        print(d)


import functools

class Solution:
    grid = None
    m = {}
    def numEnclaves(self, A: List[List[int]]) -> int:
        Solution.grid = A
        Solution.m = {}
        count = 0
        num_of_1 = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    num_of_1 += 1
                    if self.dfs(i, j, 0):
                        count += 1

        return num_of_1 - count

    def dfs(self, x, y, visited):

        if x < 0 or x >= len(Solution.grid) or y < 0 or y >= len(Solution.grid[0]):
            return True
        if x == 0 or y == 0 or x == len(Solution.grid)-1 or y == len(Solution.grid[0]) - 1:
            if Solution.grid[x][y] == 1:
                return True
            else:
                return False

        if Solution.grid[x][y] == 0:
            return False
        if (x, y, visited) in Solution.m:
            return Solution.m[(x,y, visited)]
        if visited & (1 << (x * len(Solution.grid) + y)):
            return False

        visited = visited | (1 << (x * len(Solution.grid) + y))
        ans = False
        for (a, b) in [(-1,0),(1,0),(0,-1),(0,1)]:
            ans = ans or self.dfs(x+a, y+b, visited)
        Solution.m[(x,y, visited)] = ans
        return ans

grid = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
# show_grid(grid)
print(Solution().numEnclaves(grid))