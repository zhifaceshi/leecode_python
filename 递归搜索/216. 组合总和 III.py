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


from typing import *
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        self.dfs(k, n, [], ret)
        return ret
    def dfs(self, k, n, state_lst, ret):
        if k < 0:
            return
        if n < 0:
            return
        if k == 0 and n == 0:
            state_lst = sorted(state_lst)
            if state_lst not in ret:
                ret.append(state_lst)
        for i in range(1, 10):
            if i not in state_lst:
                if i <= n:
                    self.dfs(k-1, n-i, state_lst + [i, ], ret)

print(Solution().combinationSum3(3, 9))


