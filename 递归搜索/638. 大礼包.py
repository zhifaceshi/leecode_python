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


def build_3d_matrix(a, b, c, val=0):
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

# 超时， 38 / 52
class Solution:
    prices = None
    special = None
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        Solution.prices = price
        Solution.special = special
        return self.dfs(tuple(needs))

    @functools.lru_cache(None)
    def dfs(self, needs):
        if any([w < 0 for w in needs]):
            return MAXINF
        if all([w == 0 for w in needs]):
            return 0
        ans = MAXINF

        for i in range(len(Solution.special) + 1):
            if i != len(Solution.special):
                lst = Solution.special[i]
                t = lst[: -1]
                p = lst[-1]
                candidates = tuple([w - c for w, c in zip(needs, t)])
                a = self.dfs(candidates) + p
                ans = min(ans, a)
            else:
                count = 0
                for index in range(len(needs)):
                    count += needs[index] * Solution.prices[index]
                ans = min(ans, count)

        return ans

print(Solution().shoppingOffers([10,1,1,3,8,3],
[[0,5,6,5,6,0,14],[6,3,2,1,2,0,11],[3,5,3,3,6,6,12],[0,3,0,6,6,1,25],[4,5,3,2,3,2,15],[2,0,1,6,2,4,2],[4,2,4,5,5,5,22],[3,2,6,3,5,4,9],[4,6,4,6,2,5,1],[3,0,0,6,6,2,18],[1,4,2,3,4,4,1],[3,2,6,6,4,4,2],[1,1,0,5,5,2,15],[0,1,5,4,6,5,7],[3,5,2,4,0,5,20],[3,0,3,6,3,2,3],[5,4,1,6,6,1,7],[2,1,6,1,2,2,8],[0,5,4,3,4,4,4],[2,0,2,5,1,5,7],[4,6,5,0,3,4,19],[0,5,6,3,0,5,8],[0,5,0,0,3,4,15],[5,6,1,1,0,3,15],[1,2,0,3,1,5,12],[2,1,6,3,6,3,7],[4,6,3,3,4,3,3],[1,5,5,6,4,6,19],[4,1,5,3,3,5,25],[2,1,6,4,2,3,7],[0,0,6,2,6,0,7],[4,3,0,3,6,3,5],[4,1,1,6,2,6,10],[5,2,5,5,1,4,8],[4,1,1,2,6,0,20],[5,6,3,0,2,1,12],[2,4,4,4,5,5,11],[0,2,2,3,2,1,13],[3,3,2,5,4,3,24],[3,1,3,0,0,4,20],[3,5,2,3,2,6,1],[6,2,6,4,4,0,24],[6,1,0,2,4,2,18],[0,5,6,1,0,2,20],[0,6,0,1,2,0,16],[5,6,0,2,6,5,7],[3,5,0,0,6,1,25],[1,3,1,6,0,6,3],[0,6,0,0,6,0,23],[1,5,2,4,2,3,18],[1,1,6,4,6,4,4],[3,3,5,2,5,4,21],[5,1,3,5,1,3,8],[0,2,3,6,0,6,3],[3,0,6,4,6,5,23],[3,1,4,6,4,0,24],[0,3,1,5,4,2,8],[5,6,5,3,6,6,3],[6,3,3,0,3,2,8],[0,6,5,3,0,0,10],[2,6,0,3,2,1,2],[6,2,3,5,1,6,2],[5,5,2,4,2,3,7]]
,[3,6,1,4,5,4]))