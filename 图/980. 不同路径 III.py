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

#####################################################################################################

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx, sy = None, None
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    sx, sy = i, j
        return self.dfs(sx, sy, grid, count + 1)

    def dfs(self, x, y, grid, n):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return 0
        if grid[x][y] == -1:
            return 0
        if grid[x][y] == 2:
            if n == 0:
                return 1
            else:
                return 0


        grid[x][y] = -1
        paths = self.dfs(x+1, y, grid, n-1) + \
                self.dfs(x-1, y, grid, n - 1) + \
                self.dfs(x, y+1, grid, n - 1) + \
                self.dfs(x, y-1, grid, n - 1)
        grid[x][y] = 0
        return paths

grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(Solution().uniquePathsIII(grid))









