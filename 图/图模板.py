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
    m = {}
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ans = [self.caculate(point, target) for point in ghosts]
        d = min(ans)
        a = self.caculate([0, 0], target)
        if a >= d:
            return False
        return True

    def caculate(self, point, target):
        return abs(point[0] - target[0]) + abs(point[1] - target[1])

ghosts = [[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]]
target = [7, 7]
print(Solution().escapeGhosts(ghosts, target))