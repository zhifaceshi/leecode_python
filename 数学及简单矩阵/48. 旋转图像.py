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
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(math.ceil(n / 2)):
            for a, b, c, d in generate(i, i, n - i * 2):
                a0,a1 = a
                b0,b1 = b
                c0,c1 = c
                d0,d1 = d
                matrix[a0][a1], matrix[b0][b1], matrix[c0][c1], matrix[d0][d1] = \
                     matrix[d0][d1], matrix[a0][a1], matrix[b0][b1], matrix[c0][c1]
        # for d in matrix:
        #     print(d)

def generate(x, y, n):
    a = x, y
    b = x, y + n - 1
    c = x + n -1, y + n - 1
    d = x + n - 1, y
    for i in range(n-1):
        yield a, b, c, d
        a = a[0], a[1] + 1
        b = b[0] + 1, b[1]
        c = c[0], c[1] - 1
        d = d[0] - 1, d[1]



# for d in generate(1, 1 , 1):
#     print(d)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Solution().rotate(matrix)