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
    def leastBricks(self, wall: List[List[int]]) -> int:
        reduced_wall = []
        for w in wall:
            count = 0
            t = []
            for c in w:
                count += c
                t.append(count)
            reduced_wall.append(t)
        # for p in reduced_wall:
        #     print(p)
        dct =collections.defaultdict(int)
        for w in reduced_wall:
            if len(w) == 1:
                continue
            for a in w[:-1]:
                dct[a] += 1

        a = sorted(dct.items(), key = lambda x:x[1], reverse=True)
        if len(a) == 0:
            return len(reduced_wall)
        return len(reduced_wall) - a[0][1]




wall =  [[1,1],[2],[1,1]]

print(Solution().leastBricks(wall))