import itertools
import collections
import math
import re
import sys
from typing import List

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        shuzhi = []
        for j in range(len(grid[0])):
            maxvalue = -1
            for i in range(len(grid)):
                maxvalue = max(maxvalue, grid[i][j])
            shuzhi.append(maxvalue)
        shuiping = []
        for i in range(len(grid)):
            maxvalue = -1
            for j in range(len(grid[0])):
                maxvalue = max(maxvalue, grid[i][j])
            shuiping.append(maxvalue)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                legal_value = min(shuiping[j], shuzhi[i])
                count += (legal_value - grid[i][j])
        return count

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(Solution().maxIncreaseKeepingSkyline(grid))


