import itertools
import collections
import math
import re
import sys
import functools

MAXINF = float('inf')
MININF = -float('inf')

def read_int_lst():
    return list(map(int, input().split()))

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        grid = [[0] * n for _ in range(n)]
        count = 1
        for i in range(int(math.ceil(n / 2))):
            for x, y in generate_tuple(i, i, n - i * 2):
                grid[x][y] = count
                count += 1
        return grid

def generate_tuple( x, y, n):
    for j in range(n):
        yield x, y + j
    for i in range(1, n):
        yield x+i, y+n - 1
    for j in range(1, n):
        yield x + n - 1, y + n - j - 1
    for i in range(1, n-1):
        yield x + n - i-1, y

# for a in generate_tuple(1, 1, 1):
#     print(a)


for d in (Solution().generateMatrix(3)):
    print(d)
