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
    def singleNumber(self, nums: List[int]) -> List[int]:
        num = 0
        for n in nums:
            num ^= n
        index = 1
        t = num
        while num % 2 == 0:
            num >>= 1
            index += 1
        ans1 = 0
        for n in nums:
            a = bin(n) if n > 0 else bin(n + 2 **64)
            if a[-index] == '1':
                ans1 ^= n
        ans2 = t ^ ans1
        return [ans1, ans2]

t = [1,2,1,3,2,5]
print(Solution().singleNumber(t))
