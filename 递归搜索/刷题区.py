import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ret = set()
        counter = collections.Counter(list(tiles))
        N = len(tiles)
        self.dfs(counter, [], ret, N)
        return len(ret)
    def dfs(self,counter, state_lst,  ret, N):
        if len(state_lst) != 0:
            ret.add(tuple(state_lst))

        if len(state_lst) > N:
            return
        for key, value in counter.items():
            if value > 0:
                counter[key] -= 1
                state_lst.append(key)
                self.dfs(dict(counter), state_lst, ret, N)
                state_lst.pop()
                counter[key] += 1


s = "AAABBC"
print(Solution().numTilePossibilities(s))