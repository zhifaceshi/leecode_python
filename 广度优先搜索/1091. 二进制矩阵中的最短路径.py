import itertools
import collections
import math
import re
import sys
from typing import List

MAXINF = float('inf')
MININF = -float('inf')


def read_int_lst():
    return list(map(int, input().split()))


def build_3dmatrix(a, b, c, val=0):
    data = []
    for i in range(a):
        tt = []
        for j in range(b):
            t = []
            for k in range(c):
                t.append(val)
            tt.append(t)
        data.append(tt)
    return data


def build_2d_matrix(a, b, val=0):
    data = []
    for i in range(a):
        t = []
        for j in range(b):
            t.append(val)
        data.append(t)
    return data


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = [(0, 0)]
        visited = {(0, 0)}
        step = 0
        while len(queue) != 0:
            step += 1
            size = len(queue)
            while size != 0:
                size -= 1
                cur_x, cur_y = queue.pop(0)
                if cur_x == len(grid)-1 and cur_y == len(grid[0])-1:
                    return step
                for x, y in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]:
                    new_x = cur_x + x
                    new_y = cur_y + y
                    if new_x < 0 or new_y < 0 or new_x >= len(grid) or new_y >= len(grid[0]) \
                        or grid[new_x][new_y] == 1 or (new_x, new_y) in visited:
                        continue

                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return -1

grid = [[0,1],[1,0]]
print(Solution().shortestPathBinaryMatrix(grid))